# AtelierRelay

**Capture the idea. Build the project. Relay the work.**

AtelierRelay is a local-first Windows desktop workspace for developing ideas without losing the context around them. Notes, references, media, sketches, tools, and optional AI conversations remain connected as a thought grows into a project.

## Explore AtelierRelay

The AtelierRelay website is the best place to see the product, its workflows, and its different workspace views:

### [Visit the AtelierRelay website →](https://scuttl-e.github.io/AtelierRelay_landing/)

The website also provides the current early-access download and release information.

## What AtelierRelay does

AtelierRelay begins with a thought—an idea, task, project, or custom type—and gives it a dedicated workspace called the Atelier. Instead of scattering project context between documents, browser tabs, media folders, and AI chats, AtelierRelay keeps those materials together and provides several ways to relay the finished work elsewhere.

### Capture and organise

- Create ideas, tasks, projects, and custom thought types.
- Capture a new thought near the cursor with a global hotkey.
- Search, filter, reorder, prioritise, and complete items from Home View.
- Organise rich-text notes across multiple named tabs.
- Use formatting, highlighting, dictation, line controls, and titled code blocks.
- Dock AtelierRelay to either side of the desktop for quick access.

### Work at the scale the project needs

AtelierRelay provides three main workspace views:

- **Home View** is a compact index for creating and managing thoughts.
- **Expanded View** opens one project as a focused, scrollable workspace.
- **Fullscreen View** brings Notes, Links, Media, viewers, and supporting tools together in a configurable layout.

Fullscreen panels can be resized or hidden, and each project remembers its own layout. Minimal mode can reduce the interface further when the work itself needs more room.

### Keep project material connected

Each project can contain:

- Rich-text notes and note tabs
- Web links and supporting references
- Images, video, audio, PDFs, and other files
- Embedded or separately positioned link and media viewers
- Structured references placed directly inside Notes
- Sketches, annotations, and stacked image variants

Links and media can be opened beside the active notes or sent into Notes as connected reference blocks. Those references remain tied to their source and can carry through into PDF and HTML documents.

### Use built-in tools

The Tool-dock keeps practical tools close to the active project:

- **Calculator** for standard expressions, natural-language calculations, finance functions, conversions, and cryptocurrency lookups
- **Sketchpad** for creating visual material or annotating existing images
- **Shortcuts** for opening selected applications, files, and folders
- **Widgets** for time and date, weather, cryptocurrency prices, and project import or export

### Bring in AI when it is useful

Optional AI conversations are scoped to the active project rather than operating as a generic disconnected chat.

AtelierRelay can connect through supported API providers, custom OpenAI-compatible endpoints, or an installed Codex CLI using ChatGPT sign-in. Depending on the selected connection, the AI can work with project notes, tabs, links, supported images, code blocks, imported PDF text, and other structured context.

Three operating modes control what a conversation can do:

- **Read-only** allows analysis and suggestions without changing the project.
- **Confirm** presents supported changes for approval.
- **Autonomous** allows bounded actions within the current project.

Separate conversations can be retained for research, critique, planning, or action without rebuilding the project background each time.

AI and external services are optional. Core project data remains stored locally on the user’s computer, and connected services are used only when invoked.

### Relay the work

AtelierRelay provides several routes for moving a project onward:

- **CreatePDF** turns selected note tabs, links, media, and inline references into a styled PDF.
- **HTML export** creates a responsive, continuously scrollable document for reading across desktop and mobile devices.
- **Relay Export Bundles** package a project into a portable `.tdpack` file for backup or editable transfer to another AtelierRelay installation.
- **Repo-Link** exports project context into a structured, indexed part of a repository so compatible coding agents can discover the notes, links, media, code blocks, and instructions behind the code.

Repo-Link can add managed guidance to `AGENTS.md`, `CLAUDE.md`, or another selected instruction file. Multiple AtelierRelay projects can be linked to the same repository while keeping their context separate.

With **Two-Way Link** enabled, an in-app AI conversation can also inspect approved repository content on demand. Repository access is read-only and excludes ignored files, secrets, binaries, generated content, and other restricted material.

### Adapt the workspace

AtelierRelay includes:

- Distinct interface themes
- Optional image and video backgrounds
- UI and text scaling
- Adjustable Expanded View sizing and placement
- Persistent viewer and project layouts
- Always-on-top and display controls
- Sidebar Rail and movable Mini-Brain inactivity modes
- Customisable global shortcuts
- Planned Premium controls for full theme authoring, interface refinement, typography, and deeper PDF customisation

## Local-first by design

AtelierRelay keeps its core project data on the local computer. Notes and structured project information use local application storage, while imported media is maintained on the filesystem.

Optional AI providers and connected services communicate externally only when the user chooses to invoke them.

## Availability

AtelierRelay is being developed for Windows and is currently available as an unsigned early-access beta.

Windows may display a SmartScreen warning for unsigned builds. Downloads should only be obtained through the official AtelierRelay website and linked GitHub release pages.

## About this repository

This repository contains the static AtelierRelay product website published through GitHub Pages. It is intended as the primary visual introduction to the product.

For the complete product demonstration, current release information, and download access, visit:

### [scuttl-e.github.io/AtelierRelay_landing](https://scuttl-e.github.io/AtelierRelay_landing/)
