cnt = 1
while True:
    l, p, v = list(map(int, input().split()))   # 연속하는 p일 중, l일 동안만 캠핑자 사용 가능 / 전체 휴가는 v일
    if l+p+v == 0:
        break
    
    ans = (v // p) * l
    if v % p > l:
        ans += l
    else:
        ans += v % p
    print(f"Case {cnt}: {ans}")
    cnt += 1
    