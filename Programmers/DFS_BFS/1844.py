def solution(maps):
    from collections import deque
    answer = 1
    n, m = len(maps)-1, len(maps[0])-1
    moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    queue = deque([(0, 0)])    # queue (x, y)
    visited = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    while queue:
        current = queue.popleft()
        for move in moves:
            next = (current[0] + move[0], current[1] + move[1])
            
            if 0 <= next[0] <= n and 0 <= next[1] <= m and maps[next[0]][next[1]] >= 1:
                if visited[next[0]][next[1]] == -1:
                    queue.append(next)
                    maps[next[0]][next[1]] = maps[current[0]][current[1]] + 1
                    visited[next[0]][next[1]] = 0

    answer = maps[n][m]
    if answer == 1:
        answer = -1 
    return answer

#print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))  # 11
#print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))  # -1

# visited를 저렇게 행렬로 만들어서 visited[i][j] == -1 비교하면 효율성 통과하는데,
# visited를 그냥 list로 해서 not (i, j) in visited 로 비교하면 효율성 통과 못 함. 아무래도 not a in A가 리스트를 다 돌아서 len(A) 만큼 소요돼서 그런 듯