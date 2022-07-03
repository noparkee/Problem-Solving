n = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))[:-1]

answer = 0

for i in range(len(price)-1):
    if price[i] < price[i+1]:
        price[i+1] = price[i]

for (l, p) in zip(length, price):
    answer += l * p

print(answer)