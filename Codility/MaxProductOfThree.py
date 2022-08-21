def solution(A):
    minus_lst, plus_lst = [], []
    for a in A:
        if a < 0:
            minus_lst.append(a)
        else:
            plus_lst.append(a)
    
    minus_lst.sort()
    plus_lst.sort(reverse=True)

    candidate = []
    if 0 in A:
        candidate.append(0)
    if len(plus_lst) >= 3:
        candidate.append(plus_lst[0] * plus_lst[1] * plus_lst[2])
    if len(minus_lst) >= 3:
        candidate.append(minus_lst[-3] * minus_lst[-2] * minus_lst[-1])
    if len(plus_lst) >= 1 and len(minus_lst) >= 2:
        candidate.append(plus_lst[0] * minus_lst[0] * minus_lst[1])
    if len(plus_lst) >= 2 and len(minus_lst) >= 1:
        candidate.append(plus_lst[0] * plus_lst[1] * minus_lst[-1])
    
    return max(candidate)
