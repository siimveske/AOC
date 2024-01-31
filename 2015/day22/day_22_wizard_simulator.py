from collections import namedtuple


Player = namedtuple("Player", "hp mana")
Boss = namedtuple("Boss", "hp dmg")

MagicMissile = namedtuple("MagicMissile", "name cost damage")
Drain = namedtuple("Drain", "name cost damage heal")
Shield = namedtuple("Shield", "name cost armor time")
Poison = namedtuple("Poison", "name cost damage time")
Recharge = namedtuple("Recharge", "name cost manna time")


def fight(player, boss, active_spells, is_player_turn, cost):
    boss_hp, boss_dmg = boss.hp, boss.dmg
    player_hp, player_mana = player.hp, player.mana

    new_spells = set()
    active_items = set()

    for spell in active_spells:
        if type(spell) is Shield:
            boss_dmg -= spell.armor
            duration = spell.time - 1
            if duration > 0:
                new_spells.add(Shield(spell.cost, spell.armor, duration))
                active_items.add("Shield")

        elif type(spell) is Poison:
            boss_hp -= spell.damage
            if boss_hp <= 0:
                return cost

            duration = spell.time - 1
            if duration > 0:
                new_spells.add(Poison(spell.cost, spell.damage, duration))
                active_items.add("Poison")

        elif type(spell) is Recharge:
            player_mana += spell.manna
            duration = spell.time - 1
            if duration > 0:
                new_spells.add(Recharge(spell.cost, spell.manna, duration))
                active_items.add("Recharge")

        # if type(spell) is MagicMissile:
        #     boss_hp -= spell.damage
        #     if boss_hp <= 0:
        #         return cost
        #
        # elif type(spell) is Drain:
        #     player_hp += spell.heal
        #     boss_hp -= spell.damage
        #     if boss_hp <= 0:
        #         return cost

    CHEAPEST_SPELL = 53
    spells = [
        MagicMissile("MagicMissile", 53, 4),
        Drain("Drain", 73, 2, 2),
        Shield("Shield", 113, 7, 6),
        Poison("Poison", 173, 3, 6),
        Recharge("Recharge", 229, 101, 5)
    ]

    if is_player_turn:
        if player_mana < CHEAPEST_SPELL and not active_items:
            return float("inf")

        costs = []
        for spell in spells:
            if spell.name in active_items:
                continue
            if player_mana < spell.cost:
                continue

            if type(spell) is MagicMissile:
                boss_hp -= spell.damage
                player_mana -= spell.cost
                if boss_hp <= 0:
                    return cost
                result = fight(Player(hp=player_hp, mana=player_mana), Boss(hp=boss_hp, dmg=boss_dmg), new_spells, False, cost + spell.cost)
                costs.append(result)

            elif type(spell) is Drain:
                player_hp += spell.heal
                boss_hp -= spell.damage
                player_mana -= spell.cost
                if boss_hp <= 0:
                    return cost
                result = fight(Player(hp=player_hp, mana=player_mana), Boss(hp=boss_hp, dmg=boss_dmg), new_spells, False, cost + spell.cost)
                costs.append(result)

        return min(costs)

    else:
        player_hp -= boss_dmg
        if player_hp <= 0:
            return float("inf")
        else:
            return fight(Player(hp=player_hp, mana=player_mana), Boss(hp=boss_hp, dmg=boss_dmg), new_spells, True, cost)



def part1() -> int:
    player = Player(hp=50, mana=500)
    boss = Boss(hp=55, dmg=8)
    result = fight(player, boss, set(), True, float("inf"))
    return result


def part2() -> int:
    pass


def main():
    print("---- MAIN ----")

    solution_part1 = part1()
    print(f"Solution for Part 1: {solution_part1}")
    # assert solution_part1 == 121
    #
    # solution_part2 = part2()
    # print(f"Solution for Part 2: {solution_part2}\n")
    # assert solution_part2 == 201


if __name__ == "__main__":
    main()
