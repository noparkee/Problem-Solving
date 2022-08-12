# 그리디 + 그래프 (BFS)
from collections import deque
a, b = map(int, input().split())

queue = deque([(a, 1)])

flag = False
while queue:
    q, cnt = queue.popleft()
    if q == b:
        flag = True
        break
    if q*2 <= b:
        queue.append((q*2, cnt+1))
    if q*10+1 <= b:
        queue.append((q*10+1, cnt+1))
        
if flag:
    print(cnt)
else:
    print(-1)