import sys
import tty
import termios
import atexit

from i18n import t


def _display_width(s):
    w = 0
    for ch in s:
        if ord(ch) > 127:
            w += 2
        else:
            w += 1
    return w


def _pad_left(s, width):
    padding = max(0, width - _display_width(s))
    return " " * padding + s


def _pad_center(s, width):
    diff = max(0, width - _display_width(s))
    left = diff // 2
    right = diff - left
    return " " * left + s + " " * right


def _card_box(inner_text, label, box_w):
    lines = []
    lines.append(f"┌{'─' * box_w}┐")
    lines.append(f"│{' ' * box_w}│")
    lines.append(f"│{_pad_center(inner_text, box_w)}│")
    lines.append(f"│{' ' * box_w}│")
    lines.append(f"│{_pad_center(label, box_w)}│")
    lines.append(f"│{' ' * box_w}│")
    lines.append(f"└{'─' * box_w}┘")
    return lines


def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()


def render_preview(assignment, lang):
    n = len(assignment) // 2
    lines = []
    lines.append(t("preview_title", lang))
    lines.append("")
    for i in range(n):
        top = t(f"role_{assignment[2 * i]}", lang)
        bottom = t(f"role_{assignment[2 * i + 1]}", lang)
        label = t("preview_player", lang).format(i + 1)
        lines.append(f"  {_pad_left(label, 6)}   {_pad_left(top, 16)}   {_pad_left(bottom, 16)}")
    lines.append("")
    print("\n".join(lines))


def preview_loop(assignment, lang):
    while True:
        clear_screen()
        render_preview(assignment, lang)
        choice = input(t("preview_prompt", lang)).strip().lower()
        if choice == "a":
            return assignment
        elif choice == "r":
            return None
        elif choice == "q":
            sys.exit(0)
        else:
            print(t("error_invalid_preview", lang))
            input()


def render_card_selection(player_num, top_role, bottom_role, lang):
    box_w = 18
    lines = []
    lines.append(t("card_title", lang).format(player_num))
    lines.append("")

    top_label = t("card_top", lang)
    bottom_label = t("card_bottom", lang)
    top_name = t(f"role_{top_role}", lang)
    bottom_name = t(f"role_{bottom_role}", lang)

    top_box = _card_box(top_name, top_label, box_w)
    bottom_box = _card_box(bottom_name, bottom_label, box_w)

    for tl, bl in zip(top_box, bottom_box):
        lines.append(f"    {tl}   {bl}")

    lines.append("")
    lines.append("    " + t("card_prompt", lang))
    lines.append("")

    sys.stdout.write("\033[2J\033[H")
    sys.stdout.write("\n".join(lines))
    sys.stdout.flush()


def card_selection(player_num, top_role, bottom_role, lang):
    render_card_selection(player_num, top_role, bottom_role, lang)

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    def restore():
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    atexit.register(restore)

    try:
        tty.setcbreak(fd)
        while True:
            ch = sys.stdin.read(1)
            if ch == " ":
                top_role, bottom_role = bottom_role, top_role
                render_card_selection(player_num, top_role, bottom_role, lang)
            elif ch == "\r" or ch == "\n":
                return top_role, bottom_role
    finally:
        restore()
        atexit.unregister(restore)


def distribute_roles(assignment, lang):
    n = len(assignment) // 2
    players = []

    input(t("press_enter_start", lang))

    for i in range(n):
        clear_screen()
        top_role = assignment[2 * i]
        bottom_role = assignment[2 * i + 1]

        confirmed_top, confirmed_bottom = card_selection(i + 1, top_role, bottom_role, lang)

        players.append({
            "top": confirmed_top,
            "top_alive": True,
            "bottom": confirmed_bottom,
            "bottom_alive": True,
        })

        if i < n - 1:
            clear_screen()
            input(t("clear_screen_prompt", lang))

    return players


def render_dashboard(players, lang):
    lines = []
    lines.append(t("dashboard_title", lang))
    lines.append("")

    for i, p in enumerate(players):
        top_name = t(f"role_{p['top']}", lang)
        bottom_name = t(f"role_{p['bottom']}", lang)

        top_mark = "[x]" if not p["top_alive"] else ""
        bottom_mark = "[x]" if not p["bottom_alive"] else ""

        lines.append(f"  P{i + 1}  {top_name}{top_mark}/{bottom_name}{bottom_mark}")

    lines.append("")
    print("\n".join(lines))


def kill_role(players, player_num):
    idx = player_num - 1
    p = players[idx]
    if p["top_alive"]:
        p["top_alive"] = False
        return "t"
    elif p["bottom_alive"]:
        p["bottom_alive"] = False
        return "b"
    return None


def revive_role(players, player_num):
    idx = player_num - 1
    p = players[idx]
    if not p["bottom_alive"]:
        p["bottom_alive"] = True
        return "b"
    elif not p["top_alive"]:
        p["top_alive"] = True
        return "t"
    return None


def dashboard_loop(players, lang):
    n = len(players)
    while True:
        render_dashboard(players, lang)
        cmd = input(t("dashboard_prompt", lang)).strip().lower()

        parts = cmd.split()
        if not parts:
            continue

        action = parts[0]

        if action == "quit":
            print(t("dashboard_quit", lang))
            return
        elif action == "status":
            continue
        elif action in ("kill", "alive"):
            if len(parts) < 2:
                print(t("dashboard_invalid", lang))
                continue

            try:
                player_num = int(parts[1])
            except ValueError:
                print(t("dashboard_invalid", lang))
                continue

            if player_num < 1 or player_num > n:
                print(t("error_invalid_command_player", lang).format(n))
                continue

            if action == "kill":
                pos = kill_role(players, player_num)
                if pos is None:
                    print(t("dashboard_already_dead", lang).format(player_num))
                else:
                    pos_label = t("card_top", lang) if pos == "t" else t("card_bottom", lang)
                    print(t("dashboard_kill", lang).format(player_num, pos_label))
            else:
                pos = revive_role(players, player_num)
                if pos is None:
                    print(t("dashboard_already_alive", lang).format(player_num))
                else:
                    pos_label = t("card_top", lang) if pos == "t" else t("card_bottom", lang)
                    print(t("dashboard_revive", lang).format(player_num, pos_label))
        else:
            print(t("dashboard_invalid", lang))
