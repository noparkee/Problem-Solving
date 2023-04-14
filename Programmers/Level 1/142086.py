def solution(s):
    answer = []
    a = dict()
    for i, s_i in enumerate(s):
        if s_i not in a:
            a[s_i] = []
            answer.append(-1)
        else:
            answer.append(i - a[s_i][-1])
        a[s_i].append(i)
    
    return answer