def solution(distance, rocks, n):
    answer = 0

    rocks.sort()
    rocks = rocks + [distance]
    
    left, right = 0, distance
    while left <= right:
        mid = (left + right) // 2
        mindist, cnt, current = distance, 0, 0
        
        for r in rocks:
            if r - current < mid:
                cnt += 1
            else:
                mindist = min(mindist, r - current)
                current = r
        
        if cnt > n:
            right = mid - 1
        else:
            left = mid + 1
            answer = mindist
        
    return answer   