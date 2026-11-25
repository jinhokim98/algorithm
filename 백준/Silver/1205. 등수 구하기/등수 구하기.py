n, new_score, p = map(int, input().split())

if n == 0:
    print(1)
else:
    ranking_list = list(map(int, input().split()))

    if n == p and new_score <= ranking_list[-1]:
        print(-1)
    else:
        rank = 1

        for score in ranking_list:
            if score > new_score:
                rank += 1

        print(rank)