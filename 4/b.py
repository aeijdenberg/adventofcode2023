import sys

cards, zwinnings = [], []
for line in sys.stdin:
    line = line.strip()
    if len(line):
        blah, nums = line.split(': ')
        winnings, mine = nums.split(' | ')
        winnings = set([int(x) for x in winnings.split(' ') if len(x)])
        mine = set([int(x) for x in mine.split(' ') if len(x)])
        
        cards.append(len(winnings&mine))
        zwinnings.append(1)

for idx, zz in enumerate(cards):
    for i in range(zz):
        zwinnings[idx + 1 + i] += zwinnings[idx]

print(sum(zwinnings))
