import itertools

def solution(sizes):
    sizeSet = set(itertools.chain(*sizes))
    maximum = max(sizeSet)
    minimum = min(sizeSet)
    
    for width in range(minimum, maximum + 1):
        for height in range(minimum, maximum + 1):
            canAnswer = all(width >= size[0] and height >= size[1] or width >= size[1] and height >= size[0] for size in sizes)
            if canAnswer:
                return width * height