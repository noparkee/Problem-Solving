def solution(w,h):
    answer = w*h
    
    if w == h:
        answer -= w
    else:
        for i in range(min(w, h)+1, 0, -1):
            if w%i == 0 and h%i == 0:
                m = i   # 최대공약수
                break

        answer -= ((w//m) + (h//m) - 1) * m
    
    return answer