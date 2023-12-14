import sys

rows = []
for line in sys.stdin:
    line = line.strip()
    if len(line):
        rows.append([ch for ch in line])

for i in range(1000000000):
    dirty = True
    while dirty:
        dirty = False
        for y, row in enumerate(rows):
            for x, ch in enumerate(row):
                if ch == 'O' and y > 0 and rows[y - 1][x] == '.':
                    rows[y - 1][x] = 'O'
                    rows[y][x] = '.'
                    dirty = True

rv = 0
for x in range(len(rows[0])):
    load = 0
    for y, row in enumerate(rows):
        if row[x] == 'O':
            load += len(rows) - y
    rv += load
print(rv)