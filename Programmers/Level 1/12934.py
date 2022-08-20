def solution(n):
    import math
    a = math.sqrt(n)
    if a % 1 != 0:
        answer = -1
    else:
        answer = (a+1)**2

    return answer