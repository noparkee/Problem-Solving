def solution(arr):
    answer = 0
    m = 1
    for a in arr:
        m *= a
        
    for i in range(max(arr), m+1):
        cnt = 0
        for a in arr:
            if i % a == 0:
                cnt += 1
        if cnt == len(arr):
            return i
