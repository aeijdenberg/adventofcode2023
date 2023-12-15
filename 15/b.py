import sys

def hashit(bit):
    score = 0
    for ch in bit:
        score += ord(ch)
        score *= 17
        score %= 256
    return score


for line in sys.stdin:
    line = line.strip()
    if len(line):
        bits = line.split(',')
        rv = 0
        boxes = []
        for i in range(256):
            boxes.append([])
        for bit in bits:
            if '=' in bit:
                label, depth = bit.split('=')
                box_idx = hashit(label)
                found = False
                for idx, val in enumerate(boxes[box_idx]):
                    if val[0] == label:
                        boxes[box_idx][idx] = (label, depth)
                        found = True
                        break
                if not found:
                    boxes[box_idx].append((label, depth))
            else:
                label = bit.split('-')[0]
                box_idx = hashit(label)
                for idx, val in enumerate(boxes[box_idx]):
                    if val[0] == label:
                        del boxes[box_idx][idx]
                        break

        score = 0
        for box_idx, box in enumerate(boxes):
            for lens_idx, lens in enumerate(box):
                score += (box_idx + 1) * (lens_idx + 1) * int(lens[1])
        print(score)
