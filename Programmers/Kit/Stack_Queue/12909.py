from collections import deque

def solution(s):
    s = deque(s)    
    open = deque([])
    
    while s:
        t = s.popleft()
        if t == "(":
            open.append(t)
        else:
            if len(open) == 0:
                return False
            open.popleft()
    
    if len(open) != 0:
        return False
    
    return True