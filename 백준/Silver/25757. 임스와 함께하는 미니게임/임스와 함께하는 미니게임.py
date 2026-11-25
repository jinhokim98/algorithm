import sys

N, play = input().split()
n = int(N)
members = [sys.stdin.readline().strip() for _ in range(n)]

def gameNumber(game):
    if game == 'Y':
        return 2
    elif game == 'F':
        return 3
    elif game == 'O':
        return 4

print(len(set(members)) // (gameNumber(play) - 1))