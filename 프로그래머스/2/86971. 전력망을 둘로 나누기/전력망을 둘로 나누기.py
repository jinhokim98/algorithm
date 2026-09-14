from collections import deque
INF = float('inf')

def solution(n, wires):
    answer = INF
    
    for i in range(len(wires)):
        graph = [[] for _ in range(n + 1)]
        for idx, wire in enumerate(wires):
            if idx == i:
                continue
            start, end = wire
            graph[start].append(end)
            graph[end].append(start)        
        answer = min(answer, getDistance(n, graph))
    
    return answer

def getDistance(n, graph):
    visited = [False] * (n + 1)
    candidate = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            candidate.append(bfs(i, graph, visited))
    
    return abs(candidate[0] - candidate[1])
    
def bfs(node, graph, visited):
    queue = deque()
    queue.appendleft(node)
    visited[node] = True
    count = 1

    while queue:
        cur = queue.popleft()
        
        for neighbor in graph[cur]:
            if not visited[neighbor]:
                count += 1
                visited[neighbor] = True
                queue.append(neighbor)
                
    return count
    