import sys

def allzeros(x):
    for n in x:
        if n != 0:
            return False
    return True

def doit(nums):
    done = False
    all = [nums]
    last = nums
    while not allzeros(last):
        last = [last[i] - last[i - 1] for i in range(1, len(last))]
        all.append(last)

    last.insert(0, 0)
    i = len(all) - 1
    while i:
        all[i - 1].insert(0, all[i - 1][0] - all[i][0])
        i -= 1
        
    return all[0][0]

rv = 0
for line in sys.stdin:
    line = line.strip()
    if len(line):
        nums = [int(x) for x in line.split(" ") if x.strip()]
        rv += doit(nums)
        
print(rv)