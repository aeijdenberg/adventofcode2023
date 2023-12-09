import sys

m = {
    '2': chr(2),
    '3': chr(3),
    '4': chr(4),
    '5': chr(5),
    '6': chr(6),
    '7': chr(7),
    '8': chr(8),
    '9': chr(9),
    'T': chr(10),
    'J': chr(11),
    'Q': chr(12),
    'K': chr(13),
    'A': chr(14),
}

def scoretype(d):
    c = {}
    for ch in d:
        c[ch] = c.get(ch, 0) + 1
    
    fives, fours, threes, twos = 0, 0, 0, 0
    for _, count in c.items():
        if count == 5:
            fives += 1
        elif count == 4:
            fours += 1
        elif count == 3:
            threes += 1
        elif count == 2:
            twos += 1

    if fives:
        return chr(50)
    
    if fours:
        return chr(40)

    if threes and twos:
        return chr(30)

    if threes:
        return chr(20)

    if twos == 2:
        return chr(10)

    if twos:
        return chr(5)

    return chr(0)



class Deck:
    def __init__(self, d):
        d = [m[ch] for ch in d]
        self.d = ''.join([scoretype(d)] + d)

    def Score(self):
        return self.d

bits = []
for line in sys.stdin:
    line = line.strip()
    if len(line):
        deck, score = line.split(' ')
        bits.append((Deck(deck), int(score)))

bits.sort(key=lambda x: x[0].Score())
print(sum((i + 1) * x[1] for i, x in enumerate(bits)))
        



# 32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483
