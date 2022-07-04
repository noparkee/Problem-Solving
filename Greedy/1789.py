###

n = int(input())
if n == 1:
    print(1)
else:
    for i in range(n+1):
        s = i * (i+1) / 2
        if s > n:
            print(i-1)
            break

###