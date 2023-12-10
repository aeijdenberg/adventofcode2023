import sys

lines = []
for line in sys.stdin:
    line = line.strip()
    if len(line):
        lines.append(line)


positions = {
    '-': [(-1, 0), (1, 0)],
    '|': [(0, -1), (0, 1)],
    'L': [(0, -1), (1, 0)],
    'J': [(-1, 0), (0, -1)],
    '7': [(-1, 0), (0, 1)],
    'F': [(0, 1), (1, 0)],
}


def doit():
    for y, row in enumerate(lines):
        for x, ch in enumerate(row):
            if ch == 'S':
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        cx = x + dx
                        cy = y + dy
                        if (0 <= cx < len(row)) and (0 <= cy <= len(lines)) and not (dx == dy == 0):
                            cch = lines[cy][cx]
                            if cch == '.':
                                continue
                            if (-dx, -dy) in positions[cch]:
                                so_far = [(x, y), (cx, cy)]
                                while so_far[0] != so_far[-1]:
                                    dx = so_far[-1][0] - so_far[-2][0]
                                    dy = so_far[-1][1] - so_far[-2][1]
                                    for cd in positions[lines[so_far[-1][1]][so_far[-1][0]]]:
                                        if cd != (-dx, -dy):
                                            so_far.append((so_far[-1][0] + cd[0], so_far[-1][1] + cd[1]))
                                            break
                                return so_far



                        
                            
print((len(doit()) - 1) // 2)
                        
