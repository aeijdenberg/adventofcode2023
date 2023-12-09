import sys

class Map(object):
    def __init__(self):
        self.bits = []
    def get(self, i):
        for b in self.bits:
            if i < b[1]:
                continue
            r = i - b[1]
            if r < b[2]:
                return r + b[0]
        return i

state = 0
maps = {}
for line in sys.stdin:
    line = line.strip()
    if len(line):
        if state == 0:
            if line.startswith("seeds: "):
                seeds = [int(x) for x in line.split(": ")[1].split(' ')]
                state = 1
        elif state == 1:
            if line.endswith(' map:'):
                mm = Map()
                maps[line.split(' ')[0]] = mm
            else:
                mm.bits.append([int(x) for x in line.split(' ')])

order = [
    'seed-to-soil',
    'soil-to-fertilizer',
    'fertilizer-to-water',
    'water-to-light',
    'light-to-temperature',
    'temperature-to-humidity',
    'humidity-to-location',
]

all = []
for seed in seeds:
    x = seed
    for o in order:
        x = maps[o].get(x)
    all.append(x)
print(min(all))
   