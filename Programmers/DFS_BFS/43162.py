def solution(n, computers):
    answer = 1
    link = {}
    for i in range(n):
        link[i] = [i]
    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j] == 1:
                link[i].append(j)
                link[j].append(i)
    
    stack, visited = [0], []
    while stack:
        t = stack.pop()
        if not t in visited:
            visited.append(t)
            stack += set(link[t]) - set(visited)
        
        if len(stack) == 0 and len(visited) != n:
            answer += 1
            visited.sort()
            for i in range(n):
                if not i in visited:
                    stack = [i]
                    break
    
    return answer

#print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))   # 2
#print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))   # 1
#print(solution(1, [[1]]))  # 1
#print(solution(3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]))   # 3