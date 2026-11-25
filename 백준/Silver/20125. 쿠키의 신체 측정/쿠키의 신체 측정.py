import sys

n = int(input())
matrix = [list(sys.stdin.readline().strip()) for _ in range(n)]

find_head = None

for i in range(n):
    for j in range(n):
        if matrix[i][j] == '*':
            find_head = (i, j)
            break

    if find_head is not None:
        break

heart = (find_head[0] + 1, find_head[1])

left_arm = 0
right_arm = 0

for i in range(heart[1] - 1, -1, -1):
    if matrix[heart[0]][i] == '*':
        left_arm += 1

for i in range(heart[1] + 1, n):
    if matrix[heart[0]][i] == '*':
        right_arm += 1

waist = heart
waist_length = 0

for i in range(heart[0] + 1, n):
    if matrix[i][heart[1]] == '*':
        waist = (i, heart[1])
        waist_length += 1

left_leg = (waist[0] + 1, waist[1] - 1)
right_leg = (waist[0] + 1, waist[1] + 1)

left_leg_length = 0
right_leg_length = 0

for i in range(left_leg[0], n):
    if matrix[i][left_leg[1]] == '*':
        left_leg_length += 1

for i in range(right_leg[0], n):
    if matrix[i][right_leg[1]] == '*':
        right_leg_length += 1

print(heart[0] + 1, heart[1] + 1)
print(left_arm, right_arm, waist_length, left_leg_length, right_leg_length)

