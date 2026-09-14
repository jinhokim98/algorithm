import heapq

directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

INF = float('inf')

def solution(board):
    n = len(board)
    pq = []

    distance = [[[INF] * 4 for _ in range(n)] for _ in range(n)]

    for d in range(4):
        distance[0][0][d] = 0
        heapq.heappush(pq, (0, 0, 0, d))

    while pq:
        curCost, x, y, curDir = heapq.heappop(pq)

        if curCost > distance[x][y][curDir]:
            continue

        for nextDir, (dx, dy) in enumerate(directions):
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if board[nx][ny] == 1:
                continue

            if curDir == nextDir:
                nextCost = curCost + 100
            else:
                nextCost = curCost + 600

            if nextCost < distance[nx][ny][nextDir]:
                distance[nx][ny][nextDir] = nextCost
                heapq.heappush(
                    pq,
                    (nextCost, nx, ny, nextDir)
                )

    return min(distance[n - 1][n - 1])