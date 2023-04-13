from collections import deque

def solution(n, edge):
    answer = 0
    cost = [n+1 for _ in range(n)]
    graph = {}
    for e1, e2 in edge:
        if not e1 in graph:
            graph[e1] = deque([e2])
        else:
            graph[e1].append(e2)
        
        if not e2 in graph:
            graph[e2] = deque([e1])
        else:
            graph[e2].append(e1)
    
    queue = deque([])
    queue.append((1, 0))    # (node_id, cost)
    
    while queue:
        node = queue.popleft()
        
        if cost[node[0]-1] == n+1:      # 방문한 적 없는 노드라면,
            cost[node[0]-1] = node[1]
            
            for g in graph[node[0]]:    # 이웃 노드 추가하기
                queue.append((g, node[1]+1))
        
        else:
            if node[1] < cost[node[0]-1]:
                cost[node[0]-1] = node[1]

    max_cost = max(cost)
    for c in cost:
        if c == max_cost:
            answer += 1
        
    return answer