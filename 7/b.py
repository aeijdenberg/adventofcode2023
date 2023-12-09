import sys

m = {
    'J': chr(1),
    '2': chr(2),
    '3': chr(3),
    '4': chr(4),
    '5': chr(5),
    '6': chr(6),
    '7': chr(7),
    '8': chr(8),
    '9': chr(9),
    'T': chr(10),
    'Q': chr(12),
    'K': chr(13),
    'A': chr(14),
}

def scoretype(d):
    c = {}
    for ch in d:
        c[ch] = c.get(ch, 0) + 1
    
    fives, fours, threes, twos, jokers = 0, 0, 0, 0, 0
    for ch, count in c.items():
        if ch == chr(1): # joker
            jokers = count
        elif count == 5:
            fives += 1
        elif count == 4:
            fours += 1
        elif count == 3:
            threes += 1
        elif count == 2:
            twos += 1

    if fives or (fours and jokers) or (threes and jokers >= 2) or (twos and jokers >= 3) or (jokers >= 4):
        return chr(50)
    
    if fours or (threes and jokers) or (twos and (jokers >= 2)) or jokers >= 3:
        return chr(40)

    if threes and twos or (jokers >= 1 and twos >= 2) or (jokers >= 2 and twos == 1) or jokers >= 3:
        return chr(30)

    if threes or (twos and jokers) or (jokers >= 2):
        return chr(20)

    if twos > 1 or (jokers and twos) or (jokers >= 2): 
        return chr(10)

    if twos or jokers:
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
        
# 255141151 too low
# 254853684 too low
# 255301470 TOO LOW
# 255447514 WRONG
# 255464855 WRONG

# 32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483
