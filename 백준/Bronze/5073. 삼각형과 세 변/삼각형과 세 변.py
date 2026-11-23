import sys

input = sys.stdin.readline

while True:
    lines = list(map(int, input().split()))

    if lines == [0, 0, 0]:
        break

    a, b, c = sorted(lines)

    if a + b <= c:
        print('Invalid')
    elif a == b == c:
        print('Equilateral')
    elif a == b or b == c or c == a:
        print('Isosceles')
    else:
        print('Scalene')