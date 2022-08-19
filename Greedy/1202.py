import heapq
import sys

n, k = map(int, input().split())
ans = 0

jewel_lst, c_lst = [], []
for i in range(n):
    m, v = map(int, sys.stdin.readline().split())
    heapq.heappush(jewel_lst, (m,v))
for i in range(k):
    heapq.heappush(c_lst, int(sys.stdin.readline()))

tmp_jewel = []
for i in range(k):
    c = heapq.heappop(c_lst)
    
    while jewel_lst and c >= jewel_lst[0][0]:   # heap이니까 0번째는 최소로 유지
        m, v = heapq.heappop(jewel_lst)
        heapq.heappush(tmp_jewel, -v)
    
    if tmp_jewel:
        ans -= heapq.heappop(tmp_jewel)
    elif not jewel_lst:
        break
    
print(ans)
