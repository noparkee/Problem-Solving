n = int(input())
time = list(map(int, input().split()))
total = 0

time.sort()

for t in time:
    total += t * n
    n -= 1

print(total)