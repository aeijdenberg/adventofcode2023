import sys


for line in sys.stdin:
    line = line.strip()
    if len(line):
        line = line.replace(" ", "")
        if line.startswith("Time:"):
            times = [int(x.strip()) for x in line.split(":")[1].split(" ") if len(x.strip())]
        if line.startswith("Distance:"):
            distances = [int(x.strip()) for x in line.split(":")[1].split(" ") if len(x.strip())]

def ways_to_beat(time, dist):
    rv = 0
    for i in range(1, time):
        if i * (time - i) > dist:
            rv += 1
    return rv


answer = 1
for time, dist in zip(times, distances):
    answer *= ways_to_beat(time, dist)
print(answer)
