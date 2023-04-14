def solution(t, p):
    answer = 0
    len_p = len(p)
    
    total = []
    for i in range(len(t)-len(p)+1):
        total.append(t[i:i+len(p)])
    
    for t in total:
        if int(t) <= int(p):
            answer += 1
            
    return answer