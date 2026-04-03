import sys

from engine import generate_assignment
from i18n import t
from ui import preview_loop, distribute_roles, dashboard_loop


def select_language():
    while True:
        choice = input(t("prompt_language", "en")).strip()
        if choice == "1":
            return "en"
        elif choice == "2":
            return "zh"
        else:
            print(t("error_invalid_language", "en"))


def select_player_count(lang):
    while True:
        try:
            n = int(input(t("prompt_player_count", lang)))
            if n in (6, 8):
                return n
            else:
                print(t("error_player_count", lang))
        except ValueError:
            print(t("error_player_count", lang))


def main():
    lang = select_language()
    player_count = select_player_count(lang)

    while True:
        assignment = generate_assignment(player_count)
        result = preview_loop(assignment, lang)
        if result is not None:
            assignment = result
            break

    players = distribute_roles(assignment, lang)

    dashboard_loop(players, lang)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()
        sys.exit(0)
