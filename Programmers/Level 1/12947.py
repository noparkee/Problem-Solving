def solution(x):
    h = 0
    tmp = x
    while tmp > 0:
        h += tmp % 10
        tmp = tmp // 10

    if x % h == 0:
        answer = True
    else:
        answer = False
    return answer