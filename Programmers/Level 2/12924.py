def solution(n):
    answer = 0
    total = []
    for i in range(n+1):
        total.append(i*(i+1) // 2)
    
    for i in range(n, -1, -1):
        for j in range(i-1, -1, -1):
            if total[i] - total[j] == n:
                answer += 1
            if total[i] - total[j] > n:
                break
                
    return answer