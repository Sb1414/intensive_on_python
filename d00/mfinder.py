with open('m.txt', 'r') as file:
    content = file.readlines()

array = [line.strip() for line in content]
print(array)