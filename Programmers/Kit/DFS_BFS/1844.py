from collections import deque

def solution(maps):
    answer = -1
    n, m = len(maps), len(maps[0])
    
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0, 1)])  # (x, y, cost)
    visited = [[0 for _ in range(m)] for _ in range(n)]
    
    while queue:
        node = queue.popleft()
        
        if (node[0] == n-1) and (node[1] == m-1):
            answer = node[2]    
            
        if visited[node[0]][node[1]] == 0:
            visited[node[0]][node[1]] = 1
            for move in movements:
                x = node[0] + move[0]
                y = node[1] + move[1]
                if x < 0 or x >=n or y < 0 or y >= m:
                    continue
                if maps[x][y] == 0:
                    continue
                if visited[x][y] == 1:
                    continue
                queue.append((x, y, node[2]+1))
    
    return answer