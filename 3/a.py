import sys

bits = []
for line in sys.stdin:
    line = line.strip()
    if len(line):
        bits.append(line)

sum = 0
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
                if bits[y][start - 1] != '.':
                    adj = True
            if x + 1 < len(bits[y]):
                if bits[y][x] != '.':
                    adj = True
            if y > 0:
                for x1 in range(start - 1, x + 1):
                    if x1 >= 0 and x1 < len(bits[y - 1]):
                        if bits[y - 1][x1] != '.':
                            adj = True
            if y + 1 < len(bits):
                for x1 in range(start - 1, x + 1):
                    if x1 >= 0 and x1 < len(bits[y + 1]):
                        if bits[y + 1][x1] != '.':
                            adj = True

            if adj:
                sum += number

        elif bits[y][x] == '.':
            x += 1
        else: # symbol
            x += 1

print(sum)
