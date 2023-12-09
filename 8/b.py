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

curs = [x for x in nodes.keys() if x.endswith('A')]

firsts = []
deltas = []
for z in curs:
    count = 0
    # zstops = set()
    # last = 0

    first = None
    delta = None
    while delta is None:
        z = nodes[z][{'R': 1, 'L': 0}[instructions[count % len(instructions)]]]
        if z.endswith('Z'):
            if first is None:
                first = count
            else:
                delta = count - first
        count += 1
    firsts.append(first)
    deltas.append(delta)

import math
print(math.lcm(*deltas))
