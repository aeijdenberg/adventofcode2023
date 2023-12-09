import sys

nodes = {}
for line in sys.stdin:
    line = line.strip()
    if len(line):
        bits = line.split(' = ')
        if len(bits) == 1:
            instructions = line
        elif len(bits) == 2:
            nodes[bits[0]] = bits[1][1:-1].split(', ')

count = 0
cur = 'AAA'
while cur != 'ZZZ':
    cur = nodes[cur][{'R': 1, 'L': 0}[instructions[count % len(instructions)]]]
    print(cur)
    count += 1
print(count)
