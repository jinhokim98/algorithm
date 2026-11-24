import sys

n = int(input())
weight_list = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]
answer = [1 for _ in range(n)]

for i in range(len(weight_list)):
    for j in range(len(weight_list)):
        if i == j:
            continue
        
        if weight_list[i][0] < weight_list[j][0] and weight_list[i][1] < weight_list[j][1]:
            answer[i] += 1

print(" ".join(map(str, answer)))
