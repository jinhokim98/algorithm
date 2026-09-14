from itertools import permutations

def solution(k, dungeons):
    answer = 0
    npr = list(permutations(dungeons, len(dungeons)))
    
    for case in npr:
        exploration = 0
        curFatigue = k
        
        for enter, discount in case:
            if curFatigue >= enter:
                exploration += 1
                curFatigue -= discount
        
        answer = max(answer, exploration)

    return answer