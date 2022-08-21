def solution(A):
    tmp = {}
    for a in A:
        if not a in tmp:
            tmp[a] = 1
        else:
            tmp[a] += 1
    
    tmp = list(tmp.items())
    for t in tmp:
        if t[1] % 2 == 1:
            return t[0]