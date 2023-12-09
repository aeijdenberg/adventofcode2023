z = {
    b'0': 0,
    b'1': 1,
    b'2': 2,
    b'3': 3,
    b'4': 4,
    b'5': 5,
    b'6': 6,
    b'7': 7,
    b'8': 8,
    b'9': 9,
    b'zero': 0,
    b'one': 1,
    b'two': 2,
    b'three': 3,
    b'four': 4,
    b'five': 5,
    b'six': 6,
    b'seven': 7,
    b'eight': 8,
    b'nine': 9,
}

s = 0
for line in open('in', 'rb'):
    if len(line.strip()):
        first, last = None, None

        for idx in range(len(line)):
            for k, v in z.items():
                if line[idx:].startswith(k):
                    if first is None:
                        first = v
                    last = v
        
        s += first * 10 + last
print(s)