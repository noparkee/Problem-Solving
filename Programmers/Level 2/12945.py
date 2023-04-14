def solution(n):
    answer = 0
    f = [0, 1]
    while len(f) != (n+1):
        f.append((f[-1] + f[-2]) % 1234567)
    answer = f[n]
    return answer