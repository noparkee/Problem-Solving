def solution(n):
    answer = ''
    available = ['1', '2', '4']
    num, cnt = 0, 1     # cnt를 통해서 몇 자리인지
    while True:
        if num + 3**cnt >= n:
            break
        num += 3**cnt
        cnt += 1

    r = n-num
    tmp = []
    while cnt > 0:
        if r % 3**(cnt-1) == 0:
            answer += available[r // 3**(cnt-1) - 1]    # -1 해주는게 포인트
        else:
            answer += available[r // 3**(cnt-1)]
        r = r % 3**(cnt-1)
        cnt -= 1
    
    return answer