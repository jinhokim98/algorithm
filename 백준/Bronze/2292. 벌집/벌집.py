n = int(input().strip())

answer = 1
curNum = 1

while curNum < n:
    curNum += 6 * answer
    answer += 1

print(answer)
