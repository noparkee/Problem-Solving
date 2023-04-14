def solution(k, tangerine):
    answer = 0
    size = dict()
    for t in tangerine:
        if t not in size:
            size[t] = 0
        size[t] += 1
    
    sorted_size = sorted(size.items(), key=lambda item: -item[1])
    
    for item in sorted_size:
        if k <= 0:
            break
        k -= item[1]
        answer += 1
        
    return answer