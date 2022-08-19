n, m = map(int, input().split())    # N개의 기타줄 구매

p_lst, i_lst = [], []
for i in range(m):
    p, i = map(int, input().split())    # 패키지(6개), 낱개 가격
    p_lst.append(p)
    i_lst.append(i)
min_p = min(p_lst)
min_i = min(i_lst)
    
if n <= 6:
    if min_p < n * min_i:
        ans = min_p
    else:
        ans = n * min_i
else:
    if min_p < 6 * min_i:
        ans = (n // 6) * min_p
        if min_p <= (n % 6) * min_i:
            ans += min_p
        else:
            ans += (n % 6) * min_i
    else:
        ans = n * min_i

print(ans)