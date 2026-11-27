n, k = list(map(int, input().split(" ")))
durability = list(map(int, input().split(" ")))

round = 1
conveyor_belt = []
zero_count = 0

for d in durability:
    conveyor_belt.append([d, False])

while True:
    # 1. 한 칸 이동, 이동했을 때 하차할 수 있다면 하차
    conveyor_belt.insert(0, conveyor_belt.pop())
    if conveyor_belt[n - 1][1] == True:
        conveyor_belt[n - 1][1] = False

    # 2. 먼저 올라간 것 이동, 이동 못하면 정지
    # 하차 칸 전 칸에만 로봇이 있을 수 있으므로 그 위치부터 시작까지
    for i in range(n - 2, -1, -1):
        if conveyor_belt[i][1] == True and conveyor_belt[i + 1][1] == False and conveyor_belt[i + 1][0] > 0:
            conveyor_belt[i][1] = False
            conveyor_belt[i + 1][1] = True
            conveyor_belt[i + 1][0] -= 1

            if conveyor_belt[i + 1][0] == 0:
                zero_count += 1

            # 끝 지점이라면 로봇 하차
            if i + 1 == n - 1:
                conveyor_belt[i + 1][1] = False
    
    # 3. 첫 칸 내구도가 0이 아니면 로봇 올림
    if conveyor_belt[0][0] > 0:
        conveyor_belt[0][1] = True
        conveyor_belt[0][0] -= 1

        if conveyor_belt[0][0] == 0:
            zero_count += 1
    
    # 4. 내구도 0이 k개 이상이면 종료, 아니면 반복
    if zero_count >= k:
        break
    else:
        round += 1

print(round)
