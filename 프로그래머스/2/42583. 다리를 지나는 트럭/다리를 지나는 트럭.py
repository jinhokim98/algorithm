from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    time = 0

    while queue or sum(bridge) > 0:
        bridge.popleft()

        if queue and sum(bridge) + queue[0] <= weight:
            truck = queue.popleft()
            bridge.append(truck)
        else:
            bridge.append(0)

        time += 1

    return time