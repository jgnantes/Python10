from typing import Callable, Any


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
    def enchantment_applier(item_name: str):
        """ """
        return f"{enchantment_type} {item_name}"
    return enchantment_applier


def memory_vault() -> dict[str, Callable]:
    """ """
    vault: dict = dict()
    def store(key: str, value: Any):
        """ """
        vault[key] = value
    def recall(key: str) -> Any | str:
        if key in vault:
            return vault[key]
        return "Memory not found"
    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting mage counter...")
    accum = spell_accumulator(100)
    print(f"Base 100, add 20: {accum(20)}")
    print(f"Base 100, add 30: {accum(30)}")

    print("\nTesting enchantment factory...")
    flaming_factory = enchantment_factory("Flaming")
    frozen_factory = enchantment_factory("Frozen")
    print(flaming_factory("Sword"))
    print(frozen_factory("Shield"))

    print("\nTesting memory vault...")
    mv = memory_vault()
    store = mv["store"]
    recall = mv["recall"]
    print("Store 'secret' = 42")
    store("secret", 42)
    print(f"Recall 'secret': {recall('secret')}")
    print(f"Recall 'unknown': {recall('unknown')}")