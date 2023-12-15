import sys

for line in sys.stdin:
    line = line.strip()
    if len(line):
        bits = line.split(',')
        rv = 0
        for bit in bits:
            score = 0
            for ch in bit:
                score += ord(ch)
                score *= 17
                score %= 256
            rv += score
        print(rv)
