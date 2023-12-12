import sys


def doit(line):
    springs, nums = line.split(' ')
    nums = [int(x) for x in nums.split(',')]
    for comb in range(1 << springs.count('?')):
        unknownMask = 1
        counts = []
        lastBad = 0
        for i, ch in enumerate(springs):
            if ch == '?':
                damaged = comb & unknownMask
                unknownMask <<= 1
            else:
                damaged = ch == '#'
            if damaged:
                lastBad += 1
            else:
                if lastBad:
                    counts.append(lastBad)
                    lastBad = 0
        if lastBad:
            counts.append(lastBad)

        if counts == nums:
            yield comb

rv = 0
for line in sys.stdin:
    line = line.strip()
    if len(line):
        for x in doit(line):
            rv += 1

print(rv)
