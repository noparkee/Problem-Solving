def solution(n):
    answer = 0
    d = [1, 2]
    if n <= 2:
        return d[n-1]
    
    while len(d) != n:
        d.append((d[-1] + d[-2]) % 1234567)
    answer = d[n-1]
    
    return answer