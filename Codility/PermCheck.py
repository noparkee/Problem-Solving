def solution(A):
    gt = [i for i in range(1, len(A)+1)]
    A.sort()

    if A == gt:
        return 1
    else:
        return 0
