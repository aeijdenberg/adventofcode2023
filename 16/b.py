import sys

rows = []
for line in sys.stdin:
    line = line.strip()
    if len(line):
        rows.append([ch for ch in line])

h = len(rows)
w = len(rows[0])

def try_it(i_y, i_x, i_ld):
    dirs = []
    for row in rows:
        dirs.append([])
        for col in row:
            dirs[-1].append(set({}))


    queue = [(i_y, i_x, i_ld)]
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

    return count

answers = []
for x in range(w):
    answers.append(try_it(0, x, 't'))
    answers.append(try_it(h -  1, x, 'b'))
for y in range(h):
    answers.append(try_it(y, 0, 'l'))
    answers.append(try_it(y, w - 1, 'r'))
print(max(answers))