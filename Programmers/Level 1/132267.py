def solution(a, b, n):
    answer = 0
    while n >= a:
        get_c = n // a
        answer += b * (get_c)   # 콜라 받음
        n -= (a * get_c)    # 빈병 감소
        n += b * get_c
    return answer