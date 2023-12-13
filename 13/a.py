import sys

def transpose(rows):
    rv = [''] * len(rows[0])
    for row in rows:
        for idx, ch in enumerate(row):
            rv[idx] += ch
    return rv

def printRows(rows):
    for row in rows:
        print(row)
    print()

def findLine(rows):
    for i in range(1, len(rows)):
        if rows[i] == rows[i - 1]: # start of match
            j = 1
            match = True
            while (i - 1 - j) >= 0 and (i + j) < len(rows):
                if rows[i - 1 - j] != rows[i + j]:
                    match = False
                    break
                else:
                    j += 1
            if match:
                return i
    return -1

def scoreTable(t):
    horiz = findLine(t)
    if horiz >= 0:
        return 100 * horiz
    else:
        verts = findLine(transpose(t))
        if verts >= 0:
            return verts
        else:
            raise Foo

tables = [[]]
for line in sys.stdin:
    line = line.strip()
    if len(line) == 0:
        tables.append([])
    else:
        tables[-1].append(line)
while len(tables[-1]) == 0:
    tables = tables[:-1]

sum = 0
for t in tables:
    sum += scoreTable(t)
print(sum)