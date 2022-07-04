n = int(input())
rope = []

for i in range(n):
    rope.append(int(input()))
rope.sort()

num = rope[-1]
for r in rope:
    if num < r * n:
        num = r*n
    
    n -= 1

print(num)