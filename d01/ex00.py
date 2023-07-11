from typing import Dict

def empty(purse: Dict[str, int]):
    return {}

def add_ingot(purse: Dict[str, int]):
    new_purse = purse.copy()

    new_purse["gold_ingots"] = new_purse.get("gold_ingots", 0) + 1

    return new_purse

def get_ingot(purse: Dict[str, int]):
    new_purse = purse.copy()

    new_purse.pop("gold_ingots", None)

    return new_purse

purse = empty({})
purse = add_ingot(get_ingot(add_ingot(purse)))

print(purse)

def test_empty():
    purse = {"gold_ingots": 5, "silver_coins": 10}
    empty_purse = empty(purse)
    assert empty_purse == {}, "false"
    assert purse == {"gold_ingots": 5, "silver_coins": 10}, "false"

def test_add_ingot():
    purse = {"gold_ingots": 2}
    new_purse = add_ingot(purse)
    assert new_purse == {"gold_ingots": 3}, "false"
    assert purse == {"gold_ingots": 2}, "false"

def test_get_ingot():
    purse = {"gold_ingots": 4}
    new_purse = get_ingot(purse)
    assert new_purse == {}, "false"
    assert purse == {"gold_ingots": 4}, "false"

if __name__ == "__main__":
    test_empty()
    test_add_ingot()
    test_get_ingot()
    print("Все тесты пройдены")

