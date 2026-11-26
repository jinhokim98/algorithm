import sys
import math
import heapq

n, m = map(int, input().split())
a, b, k, g = map(int, input().split())
godula_list = list(map(int, input().split()))
street_list = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(m)
]

matrix = [[] for _ in range(n + 1)]

for street in street_list:
    start, end, dist = street
    matrix[start].append([end, dist])
    matrix[end].append([start, dist])

godula_time = {}
reduce_time = 0

for i in range(1, len(godula_list)):
    start = godula_list[i - 1]

    for end, dist in matrix[start]:
        if end == godula_list[i]:
            godula_time[(start, end)] = (reduce_time, reduce_time + dist)
            godula_time[(end, start)] = (reduce_time, reduce_time + dist)
            reduce_time += dist
            break

pq = []
distance = [math.inf for _ in range(n + 1)]

distance[a] = k
heapq.heappush(pq, (k, a))

while pq:
    cur_distance, cur_node = heapq.heappop(pq)

    if cur_distance > distance[cur_node]:
        continue

    if cur_node == b:
        break

    for next_node, dist in matrix[cur_node]:
        next_dist = cur_distance + dist

        if (cur_node, next_node) in godula_time:
            block_start, block_end = godula_time[(cur_node, next_node)]
            
            if block_start <= cur_distance < block_end:
                next_dist = block_end + dist

        if distance[next_node] > next_dist:
            distance[next_node] = next_dist
            heapq.heappush(pq, (next_dist, next_node))

print(distance[b] - k)


