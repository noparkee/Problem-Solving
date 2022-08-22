def solution(N):
    answer = 0
    sqrt = N ** (1/2)
    
    for i in range(1, int(sqrt)+1):
        if N % i == 0:
            answer += 1
    answer *= 2
    if sqrt % 1 == 0:
        answer -= 1
    return answer
