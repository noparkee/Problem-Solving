def solution(n,a,b):
    answer = 0
    total = [0 for _ in range(n)]
    total[a-1] = 1
    total[b-1] = 1
    
    while True:
        answer += 1

        tmp_total = []
        for i in range(0, len(total)-1, 2):
            if sum(total[i:i+2]) == 0:
                tmp_total.append(0)
            elif sum(total[i:i+2]) == 1:
                tmp_total.append(1)
            elif sum(total[i:i+2]) == 2:
                return answer

        total = tmp_total
