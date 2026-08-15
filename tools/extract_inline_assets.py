"""Extract embedded landing-page media into deployable static assets.

This is retained as a one-time migration record and an idempotent validator for
the resulting static asset tree. It uses Pillow only for the image conversion.
"""

from __future__ import annotations

import base64
import hashlib
import re
from io import BytesIO
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parent.parent
HTML_PATH = ROOT / "index.html"
ASSETS = ROOT / "assets"
FONT_NAMES = [
    "source-sans-3-400.ttf",
    "source-sans-3-600.ttf",
    "source-sans-3-700.ttf",
]
WEBP_NAMES = ["hero-background.webp", "repo-link-background.webp"]
PNG_NAMES = [
    "atelierrelay-mark.png",
    "home-view.webp",
    "expanded-view.webp",
    "workspace-view.webp",
    "minimal-layout.webp",
    "ai-connection.webp",
    "ai-chat.webp",
    "repo-link.webp",
    "sidebar-rail.webp",
    "mini-brain.webp",
    "themes-with-images.webp",
    "themes-without-images.png",
    "atelierrelay-mark.png",
]
DATA_URI = re.compile(r"data:([^;,\s]+)(?:;[^,\s]*)?,([^\"'\s)]+)", re.IGNORECASE)


def write_bytes(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)


def convert_png_to_webp(path: Path, payload: bytes, quality: int) -> tuple[int, int, str]:
    try:
        with Image.open(BytesIO(payload)) as image:
            image.load()
            width, height = image.size
            mode = image.mode
            image.save(path, "WEBP", quality=quality, method=6)
    except OSError as error:
        raise ValueError(f"Cannot decode {path.name}: {len(payload)} bytes, {payload[:16].hex()}") from error
    return width, height, mode


def main() -> None:
    html = HTML_PATH.read_text(encoding="utf-8")
    if not DATA_URI.search(html):
        expected = [
            *(f"assets/fonts/{name}" for name in FONT_NAMES),
            *(f"assets/images/{name}" for name in WEBP_NAMES),
            *(f"assets/images/{name}" for name in sorted(set(PNG_NAMES))),
        ]
        missing = [relative for relative in expected if not (ROOT / relative).is_file()]
        if missing:
            raise RuntimeError(f"Missing extracted assets: {', '.join(missing)}")
        print("No inline data URIs remain; extracted asset tree is complete.")
        return
    font_index = 0
    webp_index = 0
    png_index = 0
    extracted: list[tuple[str, int, str]] = []
    seen_payloads: dict[str, str] = {}

    def replace(match: re.Match[str]) -> str:
        nonlocal font_index, webp_index, png_index
        mime = match.group(1).lower()
        payload = base64.b64decode(match.group(2))
        digest = hashlib.sha256(payload).hexdigest()

        if mime == "font/ttf":
            name = FONT_NAMES[font_index]
            font_index += 1
            relative = f"assets/fonts/{name}"
            write_bytes(ROOT / relative, payload)
        elif mime == "image/webp":
            name = WEBP_NAMES[webp_index]
            webp_index += 1
            relative = f"assets/images/{name}"
            write_bytes(ROOT / relative, payload)
        elif mime == "image/png":
            name = PNG_NAMES[png_index]
            png_index += 1
            relative = f"assets/images/{name}"
            if digest not in seen_payloads:
                if name.endswith(".png"):
                    write_bytes(ROOT / relative, payload)
                    dimensions = "original PNG retained"
                else:
                    quality = 94 if name.startswith("themes-") else 96
                    width, height, mode = convert_png_to_webp(ROOT / relative, payload, quality)
                    dimensions = f"{width}x{height} {mode}"
                seen_payloads[digest] = relative
                extracted.append((relative, len(payload), dimensions))
            else:
                relative = seen_payloads[digest]
        else:
            raise ValueError(f"Unexpected embedded MIME type: {mime}")
        return relative

    updated = DATA_URI.sub(replace, html)
    if (font_index, webp_index, png_index) != (3, 2, 13):
        raise RuntimeError(
            f"Unexpected embedded-resource inventory: fonts={font_index}, webp={webp_index}, png={png_index}"
        )
    HTML_PATH.write_text(updated, encoding="utf-8", newline="\n")

    print("Extracted unique assets:")
    for relative, size, details in extracted:
        print(f"{relative}\t{size}\t{details}")


if __name__ == "__main__":
    main()
