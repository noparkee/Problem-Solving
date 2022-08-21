def solution(A):
    zero_lst, one_lst = [], []
    for i, a in enumerate(A):
        if a == 0:
            zero_lst.append(i)
        else:
            one_lst.append(i)

    answer = 0
    for z in zero_lst:
        for o in one_lst:
            if z < o:
                answer += 1

    return answer        


def solution(A):
    answer, tmp = 0, sum(A)
    for a in A:
        if a == 0:
            answer += tmp
        elif a == 1:
            tmp -= 1
    
    if answer > 1000000000:
        answer = -1

    return answer
