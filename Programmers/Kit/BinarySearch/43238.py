def solution(n, times):
    answer = 0
    
    mintime = min(times)        # 하한
    maxtime = max(times) * n    # 상한
    
    while mintime <= maxtime:
        mid = (mintime + maxtime) // 2
        
        cnt = 0
        for t in times:
            cnt += mid // t
            if cnt >= n:
                break
        
        if cnt >= n:            # 중간 시간 내에 모든 인원이 입국심사를 마칠 수 있다면, 상한을 중간 값까지 내리자!
            answer = mid
            maxtime = mid - 1
        else:                   # 중간 시간 내에 모든 인원이 입국심사를 마칠 수 없다면, 하한을 중간 값까지 올리자!
            mintime = mid + 1
    
    return answer