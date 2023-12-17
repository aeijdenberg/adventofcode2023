import sys, queue

rows = []
for line in sys.stdin:
    line = line.strip()
    if len(line):
        rows.append([int(ch) for ch in line])

dir_to_delta = {
    'n': (0, -1),
    'e': (1, 0),
    's': (0, 1),
    'w': (-1, 0),
}

allowed_dirs = {
    'n': ['e', 'w'],
    'e': ['n', 's'],
    's': ['e', 'w'],
    'w': ['n', 's'],
}

h = len(rows)
w = len(rows[0])

results = {'0_0_e': 0}

q = queue.PriorityQueue()
q.put((0, 0, 0, 'e'))
q.put((0, 0, 0, 's'))
while not q.empty():
    acc, x, y, d = q.get()
    for nd in allowed_dirs[d]:
        dx, dy = dir_to_delta[nd]
        nacc = acc            
        for jj in range(1, 11):
            nx, ny = x + (jj*dx), y + (jj*dy)
            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                break # ignore

            nacc += rows[ny][nx]
            if jj < 4:
                continue

            key = '%d_%d_%s' % (nx, ny, nd)
            if key in results:
                if results[key] <= nacc:
                    continue

            results[key] = nacc
            q.put((nacc, nx, ny, nd))

prefix = '%d_%d_' % (w - 1, h - 1)
pots = set()
for rkey, rval in results.items():
    if rkey.startswith(prefix):
        pots.add(rval)

print(min(pots))
