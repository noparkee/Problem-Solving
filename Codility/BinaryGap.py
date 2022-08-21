def solution(N):
    binary = []
    while N > 0:
        binary.append(N%2)
        N = N // 2
    
    index = []
    for i, b in enumerate(binary):
        if b == 1:
            index.append(i)
    
    answer = 0
    for i in range(len(index)-1):
        candidate = index[i+1] - index[i] - 1
        if candidate > answer:
            answer = candidate

    return answer
