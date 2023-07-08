import sys

count = int(sys.argv[1])
lines = sys.stdin.readlines()
filtered_lines = []
for line in lines[:count]:
    line = line.strip()
    if len(line) == 32 and line.startswith('00000') and not line.startswith('000000'):
        filtered_lines.append(line)
for line in filtered_lines:
    print(line)
