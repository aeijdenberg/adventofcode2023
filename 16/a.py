import sys

rows = []
for line in sys.stdin:
    line = line.strip()
    if len(line):
        rows.append([ch for ch in line])

dirs = []
for row in rows:
    dirs.append([])
    for col in row:
        dirs[-1].append(set({}))

h = len(rows)
w = len(rows[0])

queue = [(0, 0, 'l')]
while len(queue):
    y, x, ld = queue.pop()
    if y < 0 or y >= h or x < 0 or x >= w:
        continue

    if ld in dirs[y][x]:
        continue

    dirs[y][x].add(ld)
    ch = rows[y][x]
    if ch == '.':
        if ld == 'l':
            queue.append((y, x + 1, ld))
        elif ld == 'r':
            queue.append((y, x - 1, ld))
        elif ld == 't':
            queue.append((y + 1, x, ld))
        elif ld == 'b':
            queue.append((y - 1, x, ld))
        else:
            raise ld
    elif ch == '|':
        if ld == 'l' or ld == 'r':
            queue.append((y - 1, x, 'b'))
            queue.append((y + 1, x, 't'))
        elif ld == 't':
            queue.append((y + 1, x, ld))
        elif ld == 'b':
            queue.append((y - 1, x, ld))
        else:
            raise ld
    elif ch == '-':
        if ld == 't' or ld == 'b':
            queue.append((y, x - 1, 'r'))
            queue.append((y, x + 1, 'l'))
        elif ld == 'l':
            queue.append((y, x + 1, ld))
        elif ld == 'r':
            queue.append((y, x - 1, ld))
        else:
            raise ld
    elif ch == '/':
        if ld == 'l':
            queue.append((y - 1, x, 'b'))
        elif ld == 'r':
            queue.append((y + 1, x, 't'))
        elif ld == 't':
            queue.append((y, x - 1, 'r'))
        elif ld == 'b':
            queue.append((y, x + 1, 'l'))
        else:
            raise ld
    elif ch == '\\':
        if ld == 'l':
            queue.append((y + 1, x, 't'))
        elif ld == 'r':
            queue.append((y - 1, x, 'b'))
        elif ld == 't':
            queue.append((y, x + 1, 'l'))
        elif ld == 'b':
            queue.append((y, x - 1, 'r'))
        else:
            raise ld
    else:
        raise ch

count = 0
for row in dirs:
    for cell in row:
        if len(cell):
            count += 1

print(count)
