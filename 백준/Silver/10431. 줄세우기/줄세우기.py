import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for students in arr:
    caseNum = students.pop(0)
    answer = 0

    for i in range(1, len(students)):
        j = i

        while j > 0 and students[j - 1] > students[j]:
            students[j - 1], students[j] = students[j], students[j - 1]
            answer += 1
            j -= 1

    print(caseNum, answer)