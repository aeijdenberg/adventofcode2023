import sys


sum = 0
for line in sys.stdin:
    line = line.strip()
    if len(line):
        game, rest = line.split(': ')

        minThings = {}

        for bit in rest.split('; '):
            things = {}
            for blah in bit.split(', '):
                number, colour = blah.split(' ')
                things[colour] = int(number)
            
            for elfColor, elfNum in things.items():
                minThings[elfColor] = max(minThings.get(elfColor, 0), elfNum)
            
        p = 1
        for v in minThings.values():
            p *= v

        sum += p
        

print(sum)
