## Context

The current codebase consists of two nearly identical Python scripts (`En_version.py` and `ZH_version.py`) that distribute Werewolf game roles via a basic terminal interface. Each script supports 6-player and 8-player modes with hardcoded role pools and constraint validation. The UI is minimal: roles are shown one-by-one with crude screen clearing (100 print statements), and the judge has no visibility into assignments until the very end.

There is no game state management — once roles are distributed, the judge has no way to track which roles are alive or dead during gameplay.

## Goals / Non-Goals

**Goals:**
- Unified codebase with language as a runtime parameter (i18n layer)
- Judge can preview full shuffled assignment before distribution
- Players can interactively swap their two cards (top/bottom) during distribution
- Persistent judge dashboard with live alive/dead tracking and strikethrough rendering
- Terminal-only UI, no external dependencies beyond Python stdlib

**Non-Goals:**
- Web or mobile UI
- Actual game flow automation (night phases, voting, ability resolution)
- Networked multiplayer
- Player count beyond 6 and 8
- Custom role pool configuration

## Decisions

### Decision 1: File structure — flat module layout

```
main.py      ← Entry point: language select, orchestration
engine.py    ← Role pools, shuffle, constraint validation
i18n.py      ← Translation tables, t() lookup function
ui.py        ← All terminal UI: preview, distribution, dashboard
```

**Rationale:** Four focused modules is the right granularity for this scope. No need for packages or subdirectories. `ui.py` owns all terminal interaction (ANSI codes, input handling, rendering), `engine.py` owns game logic, `i18n.py` owns strings.

**Alternatives considered:**
- Single file: Too cramped given the new features.
- Package with `__init__.py`: Overkill for 4 modules.

### Decision 2: Terminal interactivity via `tty` + ANSI escape codes

Use `tty.setraw(sys.stdin.fileno())` for non-blocking key capture during card selection, and ANSI escape codes (`\033[2J`, `\033[H`) for screen clearing and cursor positioning. Restore terminal state with `tty.setcbreak()` or `termios` on exit.

**Rationale:** Works on macOS terminal out of the box with Python stdlib only. No `curses` dependency (which has Windows compatibility issues and is overkill for this use case).

**Alternatives considered:**
- `curses` module: More robust but platform-dependent, harder to debug.
- `input()` polling: Can't capture single keystrokes without Enter.

### Decision 3: Strikethrough via Unicode combining characters

Dead roles rendered using U+0336 (combining long solidus overlay) inserted between each character. Example: `V̶i̶l̶l̶a̶g̶e̶r̶`.

**Rationale:** Works in any terminal that supports Unicode (all modern terminals). No ANSI escape code needed. Simple string transformation.

**Alternatives considered:**
- ANSI strikethrough (`\033[9m`): Not supported by all terminals.
- ASCII art strikethrough (e.g., `-Villager-`): Less visually clear.

### Decision 4: Data model for player state

```python
players = [
    {"top": "Werewolf", "top_alive": True, "bottom": "Hidden Wolf", "bottom_alive": True},
    ...
]
```

**Rationale:** Flat dict per player is simple and sufficient. The dashboard reads this directly. No need for classes given the scope.

### Decision 5: Shuffle algorithm — rejection sampling

Keep the current approach: Fisher-Yates shuffle, then validate constraints. Retry on invalid result.

**Rationale:** With the current role pools (12 or 16 cards) and constraints, valid shuffles are common enough that rejection sampling converges quickly. The probability of an invalid shuffle is low enough that infinite loops are practically impossible.

**Alternatives considered:**
- Constraint satisfaction solver: Over-engineered for this scale.
- Pre-computed valid shuffles: Would work but adds complexity for no real benefit.

### Decision 6: Role names as i18n keys

Role names stored in English as canonical keys in the engine. The i18n layer translates them at display time.

```python
# engine.py returns: ["Werewolf", "Hidden Werewolf", ...]
# i18n.py translates: t("role_Werewolf", lang) → "狼人"
```

**Rationale:** Engine stays language-agnostic. Adding a new language only requires a new translation dict in `i18n.py`.

## Risks / Trade-offs

- **[Risk]** Terminal raw mode may leave terminal in broken state if process crashes. → **Mitigation:** Use `try/finally` to always restore terminal state. Register `atexit` handler as backup.
- **[Risk]** Unicode strikethrough may not render correctly in all terminals. → **Mitigation:** Fallback to `[DEAD]` prefix if rendering issues reported. Most modern terminals handle it fine.
- **[Risk]** Rejection sampling could theoretically loop forever on degenerate role pools. → **Mitigation:** Add a max-iteration guard (e.g., 10000 attempts) and raise an error if exceeded. With current pools this won't happen.
- **[Trade-off]** Flat data model (dicts) vs classes. Dicts are simpler but less type-safe. Acceptable for this scope; can refactor if complexity grows.
