n, k = map(int, input().split())
coin = []
num = 0

for i in range(n):
    coin.append(int(input()))

for j in range(1, n+1):
    if k >= coin[-j]:
        tmp = (k // coin[-j])
        num += tmp
        k -= coin[-j] * tmp

print(num)