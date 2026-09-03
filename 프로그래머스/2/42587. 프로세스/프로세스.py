from collections import deque

def solution(priorities, location):
    queue = deque()
    
    for idx, priority in enumerate(priorities):
        queue.append((idx, priority))
    
    tern = 0
    while len(queue):
        idx, priority = queue.popleft()
        
        priorityList = list(map(lambda x: x[1], queue))
        
        if priorityList and max(priorityList) > priority:
            queue.append((idx, priority))
        else:
            tern += 1
            if idx == location:
                return tern
        
        