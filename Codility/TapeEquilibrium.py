def solution(A):
    answer = len(A) * 1000
    tmp1 = 0
    tmp2 = sum(A)
    for i in range(0, len(A)-1):        # indexing을 잘못해서 한참 헤맴;
        tmp1 += A[i]
        tmp2 -= A[i]
        candidate = abs(tmp1 - tmp2)
        if candidate < answer:
            answer = candidate

    return answer
