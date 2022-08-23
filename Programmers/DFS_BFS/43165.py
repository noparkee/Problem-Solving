def solution(numbers, target):
    from collections import deque
    
    answer= 0
    queue = deque([(0, 0)])
    visited = [0 for _ in range(len(numbers)+1)]
    while queue:
        t = queue.popleft()
        if visited[t[0]] == 0:
            visited[t[0]] == 1
            if t[0]+1 <= len(numbers):
                queue.append((t[0]+1, t[1]+numbers[t[0]-1]))
                queue.append((t[0]+1, t[1]-numbers[t[0]-1]))
            else:
                if t[1] == target:
                    answer += 1

    return answer

#print(solution([1, 1, 1, 1, 1], 3))    # 5
#print(solution([4, 1, 2, 1], 4))       # 2