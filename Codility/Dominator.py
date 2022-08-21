def solution(A):
    counter = {}
    for a in A:
        if not a in counter:
            counter[a] = 1
        else:
            counter[a] += 1
    counter = list(counter.items())
    counter.sort(key=lambda x: (-x[1], x[0]))
    
    if len(counter) == 0:
        return -1
    if counter[0][1] > len(A) // 2:
        dominant = counter[0][0]
        return A.index(dominant)
    else:
        return -1