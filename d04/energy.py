def filter_wiring(*args):
    filtered_args = [] # пустой список, в который будут добавляться отфильтрованные аргументы
    for arg in args: # итерация по всем переданным аргументам
        if isinstance(arg, list): # проверка, является ли аргумент списком
            # в filtered_args добавляется новый список, содержащий только элементы типа str
            filtered_args.append([item for item in arg if isinstance(item, str)])
        else: # если аргумент не является списком
            filtered_args.append([]) # в filtered_args добавляется пустой список
    return tuple(filtered_args) # возвращается кортеж из отфильтрованных списков

def fix_wiring(cables, sockets, plugs):
    # вызов функции filter_wiring для отфильтровки списков cables, sockets и plugs.
    # Результат присваивается переменным cables, sockets и plugs.
    cables, sockets, plugs = filter_wiring(cables, sockets, plugs)
    min_length = min(len(cables), len(sockets), len(plugs)) # определение минимальной длины из трех списков cables, sockets и plugs
    result = [] # создание пустого списка result, в который будут добавляться строки с результатами

    for i in range(min_length):
        if isinstance(plugs[i], str) and isinstance(sockets[i], str): # проверка, являются ли plugs[i] и sockets[i] строками
            # добавление строки в result вида "plug {cables[i]} into {sockets[i]} using {plugs[i]}"
            result.append(f"plug {cables[i]} into {sockets[i]} using {plugs[i]}")
        else: # если хотя бы один из plugs[i] и sockets[i] не является строкой
            result.append(f"weld {cables[i]} to {sockets[i]} without plug") # добавление строки в result

    for i in range(min_length, max(len(cables), len(sockets))): # итерация от min_length до максимальной длины из списков cables и sockets
        if i < len(cables) and i < len(sockets): # проверка, существуют ли элементы в списках cables и sockets по индексу i
            result.append(f"weld {cables[i]} to {sockets[i]} without plug") # добавление строки в result
        elif i < len(cables): # если элементы есть только в списке cables
            result.append(f"plug {cables[i]} into socket{i} using {plugs[i]}") # добавление строки в result

    return result # возвращение списка result

def test1():
    plugs = ['plug1', 'plug2', 'plug3']
    sockets = ['socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable1', 'cable2', 'cable3', 'cable4']

    for c in fix_wiring(cables, sockets, plugs):
        print(c)

def test2():
    plugs = ['plugZ', None, 'plugY', 'plugX']
    sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable2', 'cable1', False]

    for c in fix_wiring(cables, sockets, plugs):
        print(c)

if __name__ == '__main__':
    test1()
    print()
    test2()
