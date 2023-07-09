with open('m.txt', 'r') as file:
    content = file.readlines()

array = [line.strip() for line in content]

if len(array) != 3 or any(len(line) != 5 for line in array):
    print("Error")
else:
    count = sum(line.count('*') for line in array)
    if count != 9:
        print("False")
        exit()
    if array[0][0] != '*' or array[0][4] != '*':
        print("False")
        exit()
    if array[1][0] != '*' or array[1][1] != '*' or array[1][3] != '*' or array[1][4] != '*':
        print("False")
        exit()
    if array[2][0] != '*' or array[2][2] != '*' or array[2][4] != '*':
        print("False")
        exit()
    print("True")
