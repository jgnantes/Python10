from functools import wraps
from typing import Callable, Any
import time


def spell_timer(func: Callable) -> Callable:
    """ """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            elapsed = time.time() - start
            print(f"Spell completed in {elapsed:.3f} seconds")
    return wrapper


def power_validator(min_power: int) -> Callable:
    """ """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = None
            for value in args:
                if isinstance(value, (int, float)):
                    power = value
                    break
            if power is None:
                for value in kwargs.values():
                    if isinstance(value, (int, float)):
                        power = value
                        break
            if power is None or power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """ """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    """ """

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """ """
        return (
            len(name) >= 3
            and any(char.isalpha() for char in name)
            and all(char.isalpha() or char.isspace() for char in name)
        )

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """ """
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":

    @spell_timer
    def fireball():
        import time
        time.sleep(0.1)
        return "Fireball cast!"

    print("Testing spell timer...")
    result = fireball()
    print(f"Result: {result}")

    print("\nTesting retrying spell...")

    attempts = [0]

    @retry_spell(3)
    def waaaagh():
        attempts[0] += 1

        if attempts[0] < 4:
            raise ValueError("Failed")

        return "Waaaaaaagh spelled !"
    print(waaaagh())

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("A1"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))
