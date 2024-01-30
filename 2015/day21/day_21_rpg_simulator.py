class Item:
    def __init__(self, name, cost, damage, armor) -> None:
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor


class Character:
    def __init__(self, hp, damage, armor) -> None:
        self.hp = hp
        self.damage = damage
        self.armor = armor


def fight(player, boss):
    player_hp = player.hp
    boss_hp = boss.hp

    while True:
        boss_hp -= max(1, player.damage - boss.armor)
        if boss_hp <= 0:
            return True
        player_hp -= max(1, boss.damage - player.armor)
        if player_hp <= 0:
            return False


def part1() -> int:
    player = Character(100, 0, 0)
    boss = Character(103, 9, 2)

    weapons = [
        Item("Dagger", 8, 4, 0),
        Item("Shortsword", 10, 5, 0),
        Item("Warhammer", 25, 6, 0),
        Item("Longsword", 40, 7, 0),
        Item("Greataxe", 74, 8, 0)
    ]

    armors = [
        Item("NOARMOR", 0, 0, 0),
        Item("Leather", 13, 0, 1),
        Item("Chainmail", 31, 0, 2),
        Item("Splintmail", 53, 0, 3),
        Item("Bandedmail", 75, 0, 4),
        Item("Platemail", 102, 0, 5)
    ]

    rings = [
        Item("HAND1", 0, 0, 0),
        Item("HAND2", 0, 0, 0),
        Item("Damage +1", 25, 1, 0),
        Item("Damage +2", 50, 2, 0),
        Item("Damage +3", 100, 3, 0),
        Item("Defense +1", 20, 0, 1),
        Item("Defense +2", 40, 0, 2),
        Item("Defense +3", 80, 0, 3)
    ]

    least_gold_to_win_fight = 100000
    for weapon in weapons:
        for armor in armors:
            for ring1 in rings:
                for ring2 in rings:
                    if ring1 == ring2:
                        continue
                    player.armor = armor.armor
                    player.damage = weapon.damage + ring1.damage + ring2.damage
                    player.armor = armor.armor + ring1.armor + ring2.armor
                    if fight(player, boss):
                        least_gold_to_win_fight = min(
                            least_gold_to_win_fight, weapon.cost + armor.cost + ring1.cost + ring2.cost
                        )
    return least_gold_to_win_fight


def part2() -> int:
    pass


def main():
    print("---- MAIN ----")

    solution_part1 = part1()
    print(f"Solution for Part 1: {solution_part1}")
    assert solution_part1 == 121

    # solution_part2 = part2()
    # print(f"Solution for Part 2: {solution_part2}\n")
    # assert solution_part2 == 705600


if __name__ == "__main__":
    main()
