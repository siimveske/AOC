SPELLS = {
    "MagicMissile": {"cost": 53,  "damage":  4, "time": 1},
    "Drain":        {"cost": 73,  "damage":  2, "heal": 2, "time": 1},
    "Shield":       {"cost": 113, "armor":   7, "time": 6},
    "Poison":       {"cost": 173, "damage":  3, "time": 6},
    "Recharge":     {"cost": 229, "manna": 101, "time": 5}
}

least_mana_used = 10000000


def fight(player_hp, player_mana, boss_hp, active_spells, is_player_turn, mana_used):
    global least_mana_used

    boss_dmg = 8
    player_armor = 0
    new_spells = dict()

    for spell, time in active_spells:
        new_time = time - 1
        if spell == "MagicMissile":
            boss_hp -= SPELLS[spell]["damage"]
        elif spell == "Drain":
            player_hp += SPELLS[spell]["heal"]
            boss_hp -= SPELLS[spell]["damage"]
        elif spell == "Shield":
            player_armor = SPELLS[spell]["armor"]
        elif spell == "Poison":
            boss_hp -= SPELLS[spell]["damage"]
        elif spell == "Recharge":
            player_mana += SPELLS[spell]["manna"]

        if new_time > 0:
            new_spells[spell] = new_time

    if boss_hp <= 0:
        if mana_used < least_mana_used:
            least_mana_used = mana_used
        return True

    if mana_used >= least_mana_used:
        return False

    if is_player_turn:
        for spell in SPELLS:
            if (spell in new_spells) or (player_mana < SPELLS[spell]["cost"]):
                continue
            new_active_spells = list(new_spells.items())
            new_active_spells.append((spell, SPELLS[spell]["time"]))
            new_player_mana = player_mana - SPELLS[spell]["cost"]
            new_used_mana = mana_used + SPELLS[spell]["cost"]
            fight(player_hp, new_player_mana, boss_hp, new_active_spells, False, new_used_mana)
    else:
        player_hp -= max(1, boss_dmg - player_armor)
        if player_hp > 0:
            fight(player_hp, player_mana, boss_hp, list(new_spells.items()), True, mana_used)


def part1() -> int:
    global least_mana_used
    fight(player_hp=50, player_mana=500, boss_hp=55, active_spells=[], is_player_turn=True, mana_used=0)
    return least_mana_used


def part2() -> int:
    pass


def main():
    print("---- MAIN ----")

    solution_part1 = part1()
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 953
    #
    # solution_part2 = part2()
    # print(f"Solution for Part 2: {solution_part2}\n")
    # assert solution_part2 == 201


if __name__ == "__main__":
    main()
