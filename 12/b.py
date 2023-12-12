import sys


def processme(springs, nums, idx, counts, badCount):
    if idx >= len(springs):
        if badCount:
            counts = counts + [badCount]
        if nums == counts:
            return 1
        else:
            return 0

    rv = 0
    if springs[idx] in '#?': # damaged
        if len(counts) < len(nums) and badCount < nums[len(counts)]:
            rv += processme(springs, nums, idx + 1, counts, badCount + 1)

    if springs[idx] in '.?': # good
        if badCount:
            if len(counts) < len(nums) and badCount == nums[len(counts)]:
                rv += processme(springs, nums, idx + 1, counts + [badCount], 0)
        else:
            rv += processme(springs, nums, idx + 1, counts, 0)

    return rv
  
def doit(line):
    rv = 0
    springs, nums = line.split(' ')

    springs = '?'.join([springs] * 5)
    nums = ','.join([nums] * 5)

    nums = [int(x) for x in nums.split(',')]

    return processme(springs, nums, 0, [], 0)

rv = 0
for line in sys.stdin:
    line = line.strip()
    if len(line):
        print(rv)
        rv += doit(line)

print(rv)
