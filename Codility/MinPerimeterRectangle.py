def solution(N):
    answer = 4*N
    sqrt = N**(1/2)
    for a in range(1, int(sqrt)+1):
        if N % a == 0:
            b = N // a
            answer = min(answer, 2 * (a+b))
    
    return answer
