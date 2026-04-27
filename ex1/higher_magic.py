from typing import Callable, List, Optional


def heal(target: str, power: int) -> Optional[str]:
    """ """
    if power < 0:
        return None
    return f"Heal restores {target} for {power} HP"


def bolganone(target: str, power: int) -> str:
    """ """
    return f"A flaming blast hits {target} for {power} HP"


def nosferatu(target: str, power: int) -> str:
    """ """
    return f"{target}'s life energy is drained for {power} HP"


def fimbulvetr(target: str, power: int) -> str:
    """ """
    return f"A roaring avalanche hits {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """ """
    if callable(spell1) and callable(spell2):
        def combined_spells(target: str, power: int) -> tuple:
            return spell1(target, power), spell2(target, power)
        return combined_spells
    raise TypeError("Error: Both arguments must be callable")


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """ """
    if callable(base_spell):
        def amplified_spell(target: str, power: int) -> str:
            """ """
            return base_spell(target, power * multiplier)
        return amplified_spell
    raise TypeError("Error: Argument 'base_spell' must be callable")


def conditional_caster(
        condition: Callable, spell: Callable) -> Callable:
    """ """
    if callable(spell) and callable(condition):
        def conditional_spell(target: str, power: int) -> str:
            """ """
            if condition(target, power):
                return spell(target, power)
            return "Spell fizzled"
        return conditional_spell
    raise TypeError("Error: Both arguments must be callable")


def spell_sequence(spells: List[Callable]) -> Callable:
    """ """
    if all(map(callable, spells)):
        def sequence_caster(target: str, power: int) -> List[str]:
            """ """
            result_list: List[str] = []
            for spell in spells:
                result_list.append(spell(target, power))
            return result_list
        return sequence_caster
    raise TypeError("Error: All arguments must be callable")


if __name__ == "__main__":
    GRIMOIRE: list = [
        heal,
        bolganone,
        nosferatu,
        fimbulvetr, 1
    ]

    print("Testing spell combiner...")
    blazing_snowfall: Callable = spell_combiner(GRIMOIRE[1], GRIMOIRE[3])
    move_1: str = ""
    for spell in blazing_snowfall('Dragon', 11):
        move_1 += spell + '\n'
    print(move_1)

    print("Testing power amplifier...")
    recover: Callable = power_amplifier(GRIMOIRE[0], 2)
    move_2: str = recover('Goblin', 14)
    print(move_2)

    print("\nTesting conditional caster...")
    vampiric_gluttony: Callable = conditional_caster(
        GRIMOIRE[0], GRIMOIRE[2])
    power_move_3 = 21
    move_3: str = vampiric_gluttony('Wizard', power_move_3)
    print(move_3)

    print("\nTesting spell sequence...")
    multispell = spell_sequence(GRIMOIRE)
    for spell in multispell('Knight', 42):
        print(spell)
