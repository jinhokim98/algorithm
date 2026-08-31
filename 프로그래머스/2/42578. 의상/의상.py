def solution(clothes):
    clothes_dict = {}
    
    for name, category in clothes:
        if category not in clothes_dict:
            clothes_dict[category] = 1
        else:
            clothes_dict[category] += 1
    
    answer = 1
    
    for count in clothes_dict.values():
        answer *= (count + 1)

    return answer - 1