import sys

def split_and_swap(string):
    words = string.split()
    length = len(words)
    part_length = length // 4
    part1 = words[:part_length]
    part2 = words[-part_length:]
    part3 = words[part_length:part_length*2]
    part4 = words[part_length*2:-part_length]
    result = ''.join(part1 + part4 + part3 + part2)
    return result

input_string = ' '.join(sys.argv[1:])
result_string = split_and_swap(input_string)
print(result_string)
