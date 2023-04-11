from collections import deque

def solution(numbers, target):
    answer = 0
    
    stack = deque([(0, 0)])     # (numbers id, 현재 노드까지의 합)
    visited = [0 for _ in range(len(numbers)+1)]
    
    while stack:
        node = stack.pop()
        if node[0] + 1 <= len(numbers):
            stack.append((node[0]+1, node[1]-numbers[node[0]]))
            stack.append((node[0]+1, node[1]+numbers[node[0]]))
        
        else:
            if node[1] == target:
                answer += 1
    
    return answer
