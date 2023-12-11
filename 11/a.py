import sys
import itertools

rows = []
for line in sys.stdin:
    line = line.strip()
    if len(line):
        rows.append(line)

galaxies = []
expanded_rows = set(range(len(rows)))
expanded_cols = set(range(len(rows[0])))
for y, row in enumerate(rows):
    for x, ch in enumerate(row):
        if ch == '#':
            galaxies.append([x, y])
            if x in expanded_cols:
                expanded_cols.remove(x)
            if y in expanded_rows:
                expanded_rows.remove(y)

row_bumps = [0] * len(galaxies)
for big_row in expanded_rows:
    for i, g in enumerate(galaxies):
        if g[1] > big_row:
            row_bumps[i] += 1

col_bumps = [0] * len(galaxies)
for big_col in expanded_cols:
    for i, g in enumerate(galaxies):
        if g[0] > big_col:
            col_bumps[i] += 1

for i, g in enumerate(galaxies):
    g[0] += col_bumps[i]
    g[1] += row_bumps[i]

sum = 0
for pA, pB in itertools.combinations(galaxies, 2):
    shortest = abs(pA[0] - pB[0]) + abs(pA[1] - pB[1])
    sum += shortest

print(sum)

