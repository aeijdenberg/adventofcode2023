import sys

bits = []
for line in sys.stdin:
    line = line.strip()
    if len(line):
        bits.append(line)

def addG(gears, y, x, num):
    k = '%d_%d' % (y, x)
    if k not in gears:
        gears[k] = []
    gears[k].append(num)

gears = {}
for y in range(len(bits)):
    x = 0
    while x < len(bits[y]):
        if bits[y][x] in '0123456789':
            # read rest of symbol
            start = x
            while x < len(bits[y]) and bits[y][x] in '0123456789':
                x += 1
            number = int(bits[y][start:x])

            # is it adjacent?
            adj = False
            if start > 1:
                if bits[y][start - 1] == '*':
                    addG(gears, y, start - 1, number)
            if x + 1 < len(bits[y]):
                if bits[y][x] != '.':
                    addG(gears, y, x, number)
            if y > 0:
                for x1 in range(start - 1, x + 1):
                    if x1 >= 0 and x1 < len(bits[y - 1]):
                        if bits[y - 1][x1] == '*':
                            addG(gears, y - 1, x1, number)
            if y + 1 < len(bits):
                for x1 in range(start - 1, x + 1):
                    if x1 >= 0 and x1 < len(bits[y + 1]):
                        if bits[y + 1][x1] == '*':
                            addG(gears, y + 1, x1, number)

        elif bits[y][x] == '.':
            x += 1
        else: # symbol
            x += 1

s = 0
for k, v in gears.items():
    if len(v) == 2:
        s += v[0] * v[1]
print(s)

