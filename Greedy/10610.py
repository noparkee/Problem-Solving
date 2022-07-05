n = list(input())
n.sort(reverse=True)

if not '0' in n:
    print(-1)
else:
    n_int = list(map(int, n))
    if sum(n_int) % 3 == 0:
        print(''.join(n))
    else:
        print(-1)