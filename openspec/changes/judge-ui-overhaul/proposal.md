## Why

The current judge experience is minimal: roles are distributed one-by-one with no preview, no persistent role tracking, and no way to manage player states during the game. The two language versions (ZH and EN) are near-duplicate files, making maintenance error-prone. This change improves the judge workflow and consolidates the architecture.

## What Changes

- **Role preview**: Before distribution, the judge can review the full shuffled assignment and accept or re-shuffle.
- **Interactive card selection**: During distribution, players can swap their two cards (top/bottom) via a visual terminal UI with animated card flip.
- **Judge dashboard**: A persistent terminal dashboard showing all players' roles with live status tracking. Dead roles display with strikethrough. Commands to mark roles alive/dead during gameplay.
- **Language selection at startup**: Judge picks English or 中文; all UI text and role names switch accordingly.
- **Architecture refactor**: Extract shared game engine (role pools, shuffle logic, constraint validation) and i18n layer. The ZH and EN versions become a single codebase with language as a runtime parameter.

## Capabilities

### New Capabilities
- `role-preview`: Judge can preview and approve/reject shuffled role assignments before distribution.
- `interactive-distribution`: Players interactively choose card order (top/bottom) during role reveal with visual terminal feedback.
- `judge-dashboard`: Persistent terminal UI showing all player roles, live alive/dead status with strikethrough rendering, and commands to update role states.
- `i18n-system`: Language selection at startup; all UI text and role names resolved through a translation layer.

### Modified Capabilities
- *(none — no existing specs to modify)*

## Impact

- **Affected files**: `En_version.py` and `ZH_version.py` will be replaced by a unified codebase (`main.py`, `engine.py`, `i18n.py`, `ui.py`).
- **Breaking**: The old standalone scripts will be removed. Users run `main.py` instead.
- **Dependencies**: No new external dependencies — uses only Python stdlib (`sys`, `random`, `os`).
