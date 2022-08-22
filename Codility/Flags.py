# task: 26%, correctness: 50%, performance: 0%
def solution(A):
    if len(A) < 3:
        return 0

    peak = []
    for i in range(1, len(A)-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            peak.append((i, A[i]))
    length = []
    for i in range(len(peak)-1):
        length.append(peak[i+1][0] - peak[i][0])

    answer = 0
    for n in range(2, len(peak)+1): # n은 개수
        cnt, previous = 0, -1
        for l in length:
            if l >= n:
                cnt += 1
            else:
                if previous != -1 and previous < n:
                    if previous + l >= n:
                        cnt += 1
            previous = l
        
        if cnt >= n-1:
            answer = n
                
    return answer


# task: 33%, correctness: 62%, performance: 0%
def solution(A):
    if len(A) < 3:
        return 0

    peak = []
    for i in range(1, len(A)-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            peak.append((i, A[i]))
    length = []
    for i in range(len(peak)-1):
        length.append(peak[i+1][0] - peak[i][0])
    if len(peak) == 1:
        return 1

    answer = 0
    for n in range(2, len(peak)+1): # n은 개수
        cnt, previous = 0, -1
        for l in length:
            if l >= n:
                cnt += 1
            else:
                if previous != -1 and previous < n:
                    if previous + l >= n:
                        cnt += 1
            previous = l
        
        if cnt >= n-1:
            answer = n
                
    return answer
