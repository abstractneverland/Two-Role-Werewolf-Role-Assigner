## 1. Project scaffolding

- [x] 1.1 Create `engine.py` with role pool definitions for 6-player and 8-player modes
- [x] 1.2 Implement `generate_assignment(player_count)` in `engine.py` with Fisher-Yates shuffle and constraint validation
- [x] 1.3 Implement `is_valid(assignment)` constraint checker in `engine.py` (no Prophet+Werewolf, at least one safe pair)
- [x] 1.4 Create `i18n.py` with English and Chinese translation tables for all role names and UI strings
- [x] 1.5 Implement `t(key, lang)` lookup function in `i18n.py`

## 2. Language selection and entry point

- [x] 2.1 Create `main.py` with language selection prompt (English / 中文)
- [x] 2.2 Add player count selection (6 or 8) in `main.py`
- [x] 2.3 Wire `main.py` to call engine and UI modules with selected language

## 3. Role preview UI

- [x] 3.1 Implement `render_preview(assignment, lang)` in `ui.py` showing full assignment table
- [x] 3.2 Implement accept/re-shuffle prompt with keyboard input handling
- [x] 3.3 Wire re-shuffle loop to regenerate assignment until judge accepts

## 4. Interactive distribution UI

- [x] 4.1 Implement terminal raw mode setup/teardown with `try/finally` and `atexit` handler
- [x] 4.2 Implement `render_card_selection(top_role, bottom_role, lang)` in `ui.py` with visual card boxes
- [x] 4.3 Implement Space key handler to swap card positions and re-render
- [x] 4.4 Implement Enter key handler to confirm selection and return top/bottom arrangement
- [x] 4.5 Implement screen clearing between players using ANSI escape codes
- [x] 4.6 Wire distribution loop: iterate through all players, collect top/bottom choices, build player state list

## 5. Judge dashboard

- [x] 5.1 Implement `render_dashboard(players, lang)` in `ui.py` with table layout
- [x] 5.2 Implement strikethrough rendering function using Unicode combining characters
- [x] 5.3 Implement `kill_role(player_num, position)` and `revive_role(player_num, position)` state mutators
- [x] 5.4 Implement command parser for dashboard: `kill <n> <t|b>`, `alive <n> <t|b>`, `status`, `quit`
- [x] 5.5 Wire dashboard main loop: render → read command → update state → re-render
- [x] 5.6 Handle invalid commands with help message and re-render

## 6. Cleanup and verification

- [x] 6.1 Remove old `En_version.py` and `ZH_version.py`
- [x] 6.2 Test 6-player flow end-to-end in English
- [x] 6.3 Test 6-player flow end-to-end in Chinese
- [x] 6.4 Test 8-player flow end-to-end in English
- [x] 6.5 Test 8-player flow end-to-end in Chinese
- [x] 6.6 Test kill/revive commands and strikethrough rendering in dashboard
- [x] 6.7 Test terminal state restoration after quit (no broken terminal)
