import sys


def processme(springs, nums, idx, counts, badCount, minDone, maxDone, running):
    if idx == len(springs):
        if badCount:
            return nums[-1] == badCount and len(nums) == (counts + 1)
        else:
            return len(nums) == counts

    if running < minDone[idx] or running > maxDone[idx]:
        return 0

    rv = 0
    if springs[idx] in '#?': # damaged
        if counts < len(nums) and badCount < nums[counts]:
            rv += processme(springs, nums, idx + 1, counts, badCount + 1, minDone, maxDone, running + 1)

    if springs[idx] in '.?': # good
        if badCount:
            if counts < len(nums) and badCount == nums[counts]:
                rv += processme(springs, nums, idx + 1, counts + 1, 0, minDone, maxDone, running)
        else:
            rv += processme(springs, nums, idx + 1, counts, 0, minDone, maxDone, running)

    return rv
  
def doit(line):
    rv = 0
    springs, nums = line.split(' ')

    springs = '?'.join([springs] * 5)
    nums = ','.join([nums] * 5)

    nums = [int(x) for x in nums.split(',')]
    
    shortest = '.'.join('#' * n for n in nums)
    rightest = (' ' * (len(springs) - len(shortest))) + shortest
    leftest = shortest + (' ' * (len(springs) - len(shortest)))

    minDone = [rightest[:i].count('#') for i in range(len(springs))]
    maxDone = [leftest[:i].count('#') for i in range(len(springs))]

    return processme(springs, nums, 0, 0, 0, minDone, maxDone, 0)

i = 0
mm = int(sys.argv[1])
idx = int(sys.argv[2])
for line in sys.stdin:
    line = line.strip()
    if len(line):
        if i % mm == idx:
            rv = doit(line)
            print(i, rv, flush=True)
        i += 1


print(rv)
