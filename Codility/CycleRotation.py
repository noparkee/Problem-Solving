def solution(A, K):
    if len(A) == 0:
        return []

    K %= len(A)
    if K == 0:
        answer = A
    else:
        answer = []
        for i in range(-K, 0):
            answer.append(A[i])
        answer += A[:len(A)-len(answer)]
    
    return answer
    