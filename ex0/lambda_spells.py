from typing import List


def artifact_sorter(artifacts: List[dict]) -> List[dict]:
    """ """
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: List[dict], min_power: int) -> List[dict]:
    """ """
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: List[str]) -> List[str]:
    """ """
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: List[dict]) -> dict:
    """ """
    return {
        'max_power': max(mages, key=lambda x: x['power'])['power'],
        'min_power': min(mages, key=lambda x: x['power'])['power'],
        'avg_power': round(
            sum(map(lambda x: x["power"], mages)) / len(mages),
            2,
        )
    }


if __name__ == "__main__":
    artifacts = [
        {'name': 'Crystal Orb', 'power': 117, 'type': 'accessory'},
        {'name': 'Water Chalice', 'power': 68, 'type': 'weapon'},
        {'name': 'Storm Crown', 'power': 92, 'type': 'focus'},
        {'name': 'Ice Wand', 'power': 111, 'type': 'armor'}]
    mages = [
        {'name': 'Kai', 'power': 96, 'element': 'wind'},
        {'name': 'Alex', 'power': 59, 'element': 'shadow'},
        {'name': 'Sage', 'power': 51, 'element': 'wind'},
        {'name': 'Luna', 'power': 57, 'element': 'ice'},
        {'name': 'Casey', 'power': 87, 'element': 'light'}]
    spells = [
        'earthquake', 'tornado', 'meteor', 'fireball']

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    mpa = sorted_artifacts[0]['name']
    mpa_power = sorted_artifacts[0]['power']
    lpa = sorted_artifacts[len(artifacts) - 1]['name']
    lpa_power = sorted_artifacts[len(artifacts) - 1]['power']
    print(f"{mpa} ({mpa_power} power) comes before {lpa} ({lpa_power} power)")

    print("\nTesting power filter...")
    threshold: int = 60
    filtered_mages = power_filter(mages, threshold)
    for mage in filtered_mages:
        print(f"{mage['name']}'s power exceeds the threshold")

    print("\nTesting spell transformer...")
    transformed_spells = spell_transformer(spells)
    for spell in transformed_spells:
        print(spell, end=" ")
    print()

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Highest power among the mages: {stats['max_power']}")
    print(f"Lowest power among the mages: {stats['min_power']}")
    print(f"Average power among the mages: {stats['avg_power']}")
