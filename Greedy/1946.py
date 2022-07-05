### - readline으로 하니까 시간초과 해결;-;

import sys

t = int(input())
for _ in range(t):
    num = 0
    n = int(input())
    rank = []
    for i in range(n):
        a, b = map(int, sys.stdin.readline().split())
        rank.append((a, b))
    rank.sort()
    
    b = rank[0][1]
    for i in range(n):
        if rank[i][1] <= b:
            b = rank[i][1]
            num += 1
    
    print(num)

###