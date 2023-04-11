from collections import deque

def solution(arr):
    arr = deque(arr)
    answer = []

    top = arr.popleft()
    answer.append(top)

    while arr:
        tmp = arr.popleft()
        if tmp != top:
            answer.append(tmp)
            top = tmp
        
    return answer