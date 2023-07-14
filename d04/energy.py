def filter_wiring(*args):
    filtered_args = []
    for arg in args:
        if isinstance(arg, list):
            filtered_args.append([item for item in arg if isinstance(item, str)])
        else:
            filtered_args.append([])
    return tuple(filtered_args)

def fix_wiring(cables, sockets, plugs):
    cables, sockets, plugs = filter_wiring(cables, sockets, plugs)
    min_length = min(len(cables), len(sockets), len(plugs))
    result = []

    for i in range(min_length):
        if isinstance(plugs[i], str) and isinstance(sockets[i], str):
            result.append(f"plug {cables[i]} into {sockets[i]} using {plugs[i]}")
        else:
            result.append(f"weld {cables[i]} to {sockets[i]} without plug")

    for i in range(min_length, max(len(cables), len(sockets))):
        if i < len(cables) and i < len(sockets):
            result.append(f"weld {cables[i]} to {sockets[i]} without plug")
        elif i < len(cables):
            result.append(f"plug {cables[i]} into socket{i} using {plugs[i]}")

    return result

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
