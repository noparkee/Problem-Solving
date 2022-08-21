def solution(X, Y, D):
    answer = (Y - X) // D
    if (Y - X) % D != 0:
        answer += 1

    return answer
