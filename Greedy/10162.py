t = int(input())
button = [300, 60, 10]
answer = [0, 0, 0]

if t % 10 != 0:
    print(-1)
else:
    for i, b in enumerate(button):
        if t >= b:
            tmp = t // b
            t -= tmp * b
            answer[i] += tmp
    
    print(*answer)