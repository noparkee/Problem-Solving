n = int(input())
num = 0

max_5 = n // 5

for i in range(max_5, -1, -1):
    tmp = n - 5*i
    
    if tmp == 0:
        num = i
        break
    elif tmp % 3 == 0:
        num = i + tmp//3
        break
    
    if i == 0:
        num = -1

print(num)