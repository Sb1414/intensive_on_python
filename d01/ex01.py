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


def split_booty(*purses: Dict[str, int]):
    # создаем три пустых кошелька
    purse1 = empty({})
    purse2 = empty({})
    purse3 = empty({})

    # распределяем слитки золота между кошельками
    for purse in purses:
        num_ingots = purse.get("gold_ingots", 0)
        # если ключ "gold_ingots" присутствует в словаре purse, то метод вернет количество слитков золота
        # если ключ отсутствует, то метод вернет значение по умолчанию, т.е. 0

        # распределяем слитки по кошелькам, чтобы разница в количестве была не больше 1
        if num_ingots % 3 == 0:
            purse1 = add_ingot(purse1)
            purse2 = add_ingot(purse2)
            purse3 = add_ingot(purse3)
        elif num_ingots % 3 == 1:
            purse1 = add_ingot(purse1)
        else:
            purse2 = add_ingot(purse2)

    # возвращаем три кошелька
    return purse1, purse2, purse3

purse1 = {"gold_ingots": 3}
purse2 = {"gold_ingots": 2}
purse3 = {"gold_ingots": 1}

result = split_booty(purse1, purse2, purse3)
print(result)
