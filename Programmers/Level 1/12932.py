def solution(n):
    n = list(str(n))
    answer = []

    for i in range(1, len(n)+1):
        answer.append(int(n[-i]))
        
    return answer