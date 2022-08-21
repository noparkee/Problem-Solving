# 50 % (시간초과)
def solution(A, B, K):
    answer = 0
    for i in range(A, B+1):
        if i % K == 0:
            answer += 1
    
    return answer


def solution(A, B, K):
    tmp = A
    while True:
        if tmp % K == 0:
            break
        tmp += 1
    
    answer = (B - tmp) // K + 1
        
    return answer
