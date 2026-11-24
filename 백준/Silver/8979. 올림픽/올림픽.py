import sys

n, k = list(map(int, input().split()))
country_list = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]

country_list.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

prev = (0, 0, 0)
answer = {}
rank = 0

for idx, country in enumerate(country_list):
    num, gold, silver, bronze = country
    prevGold, prevSilver, prevBronze = prev

    if prevGold == gold and prevSilver == silver and prevBronze == bronze:
        answer[num] = rank
    else:
        rank = idx + 1
        prev = (gold, silver, bronze)
        answer[num] = rank
    
print(answer[k])    
