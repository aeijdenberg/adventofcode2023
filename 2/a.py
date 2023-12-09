import sys

constraint = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

sum = 0
for line in sys.stdin:
    line = line.strip()
    if len(line):
        game, rest = line.split(': ')

        allGood = True
        for bit in rest.split('; '):
            things = {}
            for blah in bit.split(', '):
                number, colour = blah.split(' ')
                things[colour] = int(number)
            
            matches = True
            for elfColor, elfNum in things.items():
                if elfNum > constraint.get(elfColor, 0):
                    matches = False
            
            if not matches:
                allGood = False

        if allGood:
            id = int(game.split(' ')[1])
            
            sum += id

print(sum)
