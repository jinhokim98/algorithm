import sys

n = int(input())
switch = list(map(int, input().split(" ")))
switch.insert(0, 0)

students = int(input())

infos = [list(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(students)]

for info in infos:
    gender, number = info

    if gender == 1:
        for i in range(number, n + 1, number):
            switch[i] = 1 - switch[i]
    
    if gender == 2:
        spread = 0

        while number - spread >= 1 and number + spread <= n:
            left = number - spread
            right = number + spread

            if switch[left] != switch[right]:
                break
            
            value = 1 - switch[left]
            switch[left] = value
            switch[right] = value
            
            spread += 1

answer_list = switch[1::]
answer = []

for i in range(0, n, 20):
    print(*answer_list[i:i + 20])

