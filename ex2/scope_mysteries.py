from typing import Callable


def mage_counter() -> Callable:
    """ """
    count: int = 0
    def self_counter() -> int:
        """ """
        nonlocal count
        count += 1
        return count
    return self_counter


def spell_accumulator(initial_power: int) -> Callable:
    """ """
    result_power: int = initial_power
    def add_power(power: int) -> int:
        nonlocal result_power
        result_power += power
        return result_power
    return add_power


def enchantment_factory(enchantment_type: str) -> Callable:
    """ """


def memory_vault() -> dict[str, Callable]:
    """ """


if __name__ == "__main__":
    f1 = spell_accumulator(5)
    print(f1(5))
    print(f1(5))

    f2 = mage_counter()
    for _ in range(13):
        i = f2()
    print(i)