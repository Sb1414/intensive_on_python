with open('m.txt', 'r') as file:
    content = file.readlines()

array = [line.strip() for line in content]

if len(array) != 3 or any(len(line) != 5 for line in array):
    print("Error")
else:
    print("True")
