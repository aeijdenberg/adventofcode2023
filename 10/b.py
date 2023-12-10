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

def vertical(l):
    return l[0][0] == l[1][0]

class MathLine:
    def __init__(self, p1, p2):
        if p1[0] == p2[0]:
            self.vertical = True
            self.x = p1[0]
            self.min_y = min(p1[1], p2[1])
            self.max_y = max(p1[1], p2[1])
        else:
            self.vertical = False
            if p1[0] > p2[0]:
                p1, p2 = p2, p1
            self.a = (p2[1] - p1[1]) / (p2[0] - p1[0])
            self.b = p1[1] - (self.a * p1[0])
            self.min_x = p1[0]
            self.max_x = p2[0]

    def y(self, x):
        return self.b + (self.a * x)

    def intersects(self, other):
        if self.vertical:
            if other.vertical:
                raise WillNotHappen
            else:
                if self.x < other.min_x:
                    return False
                if self.x > other.max_x:
                    return False
                
                y = other.y(x)
                return self.min_y < y < self.max_y
        else:
            if other.vertical:
                raise WillNotHappen

            if self.a == other.a:
                if self.b != other.b:
                    return False
                
                raise PleaeDontHappen

            ix = (self.b - other.b) / (other.a - self.a)
            return (self.min_x < ix < self.max_x) and (other.min_x < ix < other.max_x)



nodes = doit()

clean = []
for y, row in enumerate(lines):
    ll = ''
    for x, ch in enumerate(row):
        if (x, y) in nodes:
            ll += lines[y][x]
        else:
            ll += '.'
    clean.append(ll)

for row in clean:
    print(row)




# less_nodes = [nodes[0]]
# for i in range(1, len(nodes) - 1):
#     if (nodes[i - 1][0] + nodes[i + 1][0] == nodes[i][0] * 2) and (nodes[i - 1][1] + nodes[i + 1][1] == nodes[i][1] * 2):
#         # then we can skip us
#         pass
#     else:
#         less_nodes.append(nodes[i])
# less_nodes.append(nodes[-1])

# nodes = less_nodes

edges = []
for i in range(1, len(nodes)):
    edges.append(MathLine(nodes[i-1], nodes[i]))

inner = 0
for y in range(len(clean)):
    row = clean[y]
    for x in range(len(row)):
        if row[x] == '.':
            count = 0
            for edge in edges:
                if edge.intersects(MathLine((-1, y + 0.5), (x, y + 0.5))):
                    count += 1
            row = row[:x] + str(count%10)[:1] + row[x+1:]
            if count % 2 == 1:
                inner += 1
    clean[y] = row
    print(row)

print(inner)