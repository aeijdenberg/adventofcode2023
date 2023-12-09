import sys

maxthing = 99999999999999999

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

for o in order:
    maps[o].bits.sort(key=lambda b: b[0])
    new_bits = []
    last_fin = 0
    for zz in maps[o].bits:
        if zz[0] > last_fin:
            new_bits.append([last_fin, last_fin, zz[0] - last_fin])
        new_bits.append(zz)
        last_fin = zz[0] + zz[2]
    new_bits.append([last_fin, last_fin, maxthing - last_fin])
    maps[o].bits = new_bits

    if maps[o].bits[0][0] != 0:
        maps[o].bits = [(0, 0, maps[o].bits[0][0])] + maps[o].bits


# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4

def calcit(seed):
    x = seed
    for o in order:
        x = maps[o].get(x)
    return x

seed_ranges = []
for i in range(len(seeds)):
    if i % 2 == 0:
        seed_ranges.append(seeds[i:i+2])
seed_ranges.sort(key=lambda x: x[0])

def trythisrange(target_low, target_high):
    #print("trying range", target_low, target_high)
    for ss, sr in seed_ranges:
        x, y = xintersect(ss, ss + sr, target_low, target_high)
        if x < 0:
            continue
        print("GOT ONE", x, calcit(x))
        sys.exit(0)

#  a...b   c...d
#  a...c...b...d
#  c...a...b...d
#  a...c...d...b
#  c...a...d...b
#  c...d   a...b
def xintersect(a, b, c, d):
    if a <= b <= c <= d:
        return -1, -1
    elif a <= c <= b <= d:
        return c, b
    elif c <= a <= b <= d:
        return a, b
    elif a <= c <= d <= b:
        return c, d
    elif c <= a <= d <= b:
        return a, d
    elif c <= d <= a <= b:
        return -1, -1
    else:
        raise Ooops
    
    

def findit(idx, target_low, target_high):
    # print(order[idx], "target", target_low, target_high)
    m = maps[order[idx]]
    for zz in m.bits:
        # print("rule", zz)
        oLow, oHigh = xintersect(target_low, target_high, zz[0], zz[0] + zz[2])
        if oLow < 0:
            # print("no match")
            continue
        # print("match", oLow, oHigh)
        
        if idx == 0:
            trythisrange(zz[1] + oLow - zz[0], zz[1] + oHigh - zz[0])
        else:
            findit(idx - 1, zz[1] + oLow - zz[0], zz[1] + oHigh - zz[0])

findit(len(order) - 1, 0, maxthing)

