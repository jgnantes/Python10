from functools import reduce, partial, lru_cache, singledispatch
from typing import Callable, Any
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    """ """
    if not spells:
        return 0
    operations: dict = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min,
    }
    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")
    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """ """
    return {
        "fire": partial(base_enchantment, 50, "Fire"),
        "ice": partial(base_enchantment, 50, "Ice"),
        "lightning": partial(base_enchantment, 50, "Lightning"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """ """
    if n < 0:
        raise ValueError("Input should be non-negative")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """ """

    @singledispatch
    def cast(spell: Any) -> str:
        """ """
        return "Unknown spell type"

    @cast.register
    def _(spell: int) -> str:
        """ """
        return f"Damage spell: {spell} damage"

    @cast.register
    def _(spell: str) -> str:
        """ """
        return f"Enchantment: {spell}"

    @cast.register
    def _(spell: list) -> str:
        """ """
        return f"Multi-cast: {len(spell)} spells"

    return cast


if __name__ == "__main__":
    spells = [10, 20, 30, 40]

    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting partial enchanter...")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"{element} enchantment with {power} power applied to {target}"
    enchanters = partial_enchanter(base_enchantment)
    print(enchanters["fire"]("Sword"))
    print(enchanters["ice"]("Shield"))
    print(enchanters["lightning"]("Staff"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["fire", "ice", "lightning"]))
    print(dispatcher(3.14))
