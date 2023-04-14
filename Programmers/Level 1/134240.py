def solution(food):
    answer = ''
    for i, f in enumerate(food):
        if i == 0:
            continue
        answer += str(i) * (f // 2)
    answer += '0'
    answer += answer[:-1][::-1]
    return answer