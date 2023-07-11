from typing import Dict

def empty(purse: Dict[str, int]) -> Dict[str, int]:
    return {}

def add_ingot(purse: Dict[str, int]) -> Dict[str, int]:
    new_purse = purse.copy()

    new_purse["gold_ingots"] = new_purse.get("gold_ingots", 0) + 1

    return new_purse

def get_ingot(purse: Dict[str, int]) -> Dict[str, int]:
    new_purse = purse.copy()

    new_purse.pop("gold_ingots", None)

    return new_purse

purse = empty({})
purse = add_ingot(get_ingot(add_ingot(purse)))

print(purse)

