def solution(N, A):
    answer = [0 for _ in range(N)]
    for a in A:
        if a == N+1:
            m = max(answer)
            answer = [m] * N
        else:
            answer[a-1] += 1
    
    return answer


# max를 계속 들고 다니도록 (함수 사용 않고)
def solution(N, A):
    max_n = 0
    answer = [0] * N
    for a in A:
        if a == N+1:
            answer = [max_n] * N
        else:
            answer[a-1] += 1
            max_n = max(max_n, answer[a-1])
    
    return answer


# answer를 새로 만드는게 아니라, 동기화 느낌으로...?
def solution(N, A):
    max, min = 0, 0
    answer = [0] * N
    for a in A:
        if a == N+1:
            min = max
        else:
            if answer[a-1] < min:
                answer[a-1] = min
            answer[a-1] += 1
            if max < answer[a-1]:
                max = answer[a-1]
    
    for i in range(len(answer)):
        if answer[i] < min:
            answer[i] = min
    
    return answer
