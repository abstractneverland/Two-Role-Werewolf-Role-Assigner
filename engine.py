import random

ROLE_POOLS = {
    6: [
        "Werewolf", "Hidden Werewolf",
        "Prophet", "Witch", "Hunter", "Guard",
        "Duplicate",
        "Villager", "Villager", "Villager", "Villager", "Villager",
    ],
    8: [
        "Werewolf", "Werewolf", "Hidden Werewolf",
        "Prophet", "Witch", "Hunter", "Guard",
        "Idiot", "Silencer",
        "Duplicate",
        "Villager", "Villager", "Villager", "Villager", "Villager", "Villager",
    ],
}

SAFE_PAIRS = {
    ("Villager", "Villager"),
    ("Duplicate", "Villager"),
    ("Villager", "Duplicate"),
}

BAD_COMBOS = {
    ("Prophet", "Werewolf"),
    ("Prophet", "Hidden Werewolf"),
    ("Werewolf", "Prophet"),
    ("Hidden Werewolf", "Prophet"),
}


def is_valid(assignment):
    has_safe = False
    for i in range(len(assignment) // 2):
        top = assignment[2 * i]
        bottom = assignment[2 * i + 1]
        if (top, bottom) in BAD_COMBOS:
            return False
        if (top, bottom) in SAFE_PAIRS:
            has_safe = True
    return has_safe


def generate_assignment(player_count, max_attempts=10000):
    pool = list(ROLE_POOLS[player_count])
    n = len(pool)
    for _ in range(max_attempts):
        for i in range(n):
            j = random.randint(i, n - 1)
            pool[i], pool[j] = pool[j], pool[i]
        if is_valid(pool):
            return list(pool)
    raise RuntimeError(
        f"Failed to generate a valid assignment after {max_attempts} attempts. "
        "This should not happen with standard role pools."
    )
