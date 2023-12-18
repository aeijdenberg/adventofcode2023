import sys

deltas = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, -1),
    'D': (0, 1),
}

path = []
for line in sys.stdin:
    line = line.strip()
    if len(line):
        dir, amt, _ = line.split(' ')
        path.append((dir, int(amt)))

minx, miny, maxx, maxy = 0, 0, 0, 0
cx, cy = 0, 0
for dir, amt in path:
    dx, dy = deltas[dir]
    cx += dx * amt
    cy += dy * amt
    minx = min(minx, cx)
    maxx = max(maxx, cx)
    miny = min(miny, cy)
    maxy = max(maxy, cy)

h = 3 + maxy - miny
w = 3 + maxx - minx

rows = []
for i in range(h):
    r = []
    for j in range(w):
        r.append('.')
    rows.append(r)

cx, cy = 1 + -minx, 1 + -miny
rows[cy][cx] = '#'
for dir, amt in path:
    dx, dy = deltas[dir]
    for i in range(amt):
        cx += dx
        cy += dy
        rows[cy][cx] = '#'

# make border B
for i in range(w):
    rows[0][i] = '+'
    rows[-1][i] = '+'
for i in range(h):
    rows[i][0] = '+'
    rows[i][-1] = '+'

dirty = True
while dirty:
    dirty = False
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            if ch == '.':
                if rows[y - 1][x] == '+' or rows[y + 1][x] == '+' or rows[y][x - 1] == '+' or rows[y][x + 1] == '+':
                    row[x] = '+'
                    dirty = True

count = 0
for row in rows:
    for ch in row:
        if ch == '+':
            count += 1
        
print((w * h) - count)
