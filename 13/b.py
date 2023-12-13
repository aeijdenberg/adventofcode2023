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

def matchWithSmudge(a, b, smudgesRemaining):
    sr = smudgesRemaining
    for ca, cb in zip(a, b):
        if ca == cb:
            continue
        else:
            if sr > 0:
                sr -= 1
                continue
            else:
                return False, 0
    return True, sr


def findLine(rows):
    for i in range(1, len(rows)):
        matches, smudges = matchWithSmudge(rows[i], rows[i - 1], 1)
        if matches: # start of match
            j = 1
            match = True
            while (i - 1 - j) >= 0 and (i + j) < len(rows):
                matches, smudges = matchWithSmudge(rows[i - 1 - j], rows[i + j], smudges)
                if not matches:
                    match = False
                    break
                else:
                    j += 1
            if match and smudges == 0:
                return i
    return -1

def scoreTable(t):
    verts = findLine(transpose(t))
    if verts >= 0:
        return verts

    horiz = findLine(t)
    if horiz >= 0:
        return 100 * horiz
    
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

# 42282 too high