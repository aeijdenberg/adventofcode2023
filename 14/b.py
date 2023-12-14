import sys


def transpose(rows):
    rv = [[] for i in range(len(rows[0]))]
    for row in rows:
        for idx, ch in enumerate(row):
            rv[idx].append(ch)
    return rv

def north(rows):
    dirty = True
    while dirty:
        dirty = False
        for y, row in enumerate(rows):
            for x, ch in enumerate(row):
                if ch == 'O' and y > 0 and rows[y - 1][x] == '.':
                    rows[y - 1][x] = 'O'
                    rows[y][x] = '.'
                    dirty = True
    return rows

def west(rows):
    return transpose(north(transpose(rows)))

def south(rows):
    return north(rows[::-1])[::-1]

def east(rows):
    return transpose(north(transpose(rows)[::-1])[::-1])

def cycle(rows):
    return east(south(west(north(rows))))

def load(rows):
    rv = 0
    for y, row in enumerate(rows):
        for ch in row:
            if ch == 'O':
                rv += len(rows) - y
    return rv

def dump(rows):
    for r in rows:
        print(''.join(r))
    print()

def hash(rows):
    return ''.join([''.join(row) for row in rows])

rows = []
for line in sys.stdin:
    line = line.strip()
    if len(line):
        rows.append([ch for ch in line])

target_runs = 1000000000
seen_to_index = {}
i = 0
while i < target_runs:
    h = hash(rows)
    if h in seen_to_index:
        last = seen_to_index[h]
        delta = i - last
        i += ((target_runs - i) // delta) * delta
    else:
        seen_to_index[h] = i
    rows = cycle(rows)
    i += 1

print(load(rows))
