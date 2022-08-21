def solution(X, A):
    answer = -1
    gt = [1 for _ in range(X)]
    sum_gt = X
    for i, a in enumerate(A):
        if gt[a-1] == 1:
            gt[a-1] = 0
            sum_gt -= 1
            if sum_gt == 0:
                answer = i
                break

    return answer
    