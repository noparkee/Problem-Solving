# 88 %
def solution(A):
    A.sort()            # A.sort()와, A = list(set(A)) 위치 바꾸면 100 %
    A = list(set(A))
    cnt = 1
    answer = -1
    for a in A:
        if a > 0:
            if a != cnt:
                answer = cnt
                break
            cnt += 1
    
    if answer == -1:
        answer = cnt
    
    return answer


# 100 %
def solution(A):
    A.sort()
    A = list(set(A))
    answer = 1
    for a in A:
        if a == answer:
            answer += 1
    
    return answer
    