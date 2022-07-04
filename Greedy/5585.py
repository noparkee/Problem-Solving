n = int(input())
change = 1000-n
coin = [500, 100, 50, 10, 5, 1]

num = 0

for c in coin:
    tmp = change // c
    if tmp != 0:
        num += tmp
        change -= c * tmp

print(num)