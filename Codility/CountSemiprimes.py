# task: 66%, correctness: 100%, performace: 40%
def solution(N, P, Q):
    # semiprime은 prime의 곱으로 만들어진 것들
    prime = [True] * (N+ 1)
    prime[0] = prime[1] = False
    i = 2
    while (i * i <= N):
        if (prime[i]):
            k = i * i
            while (k <= N):
                prime[k] = False
                k += i
        i += 1
    # prime[i]: i가 prime number인지 아닌지

    semiprime = [False] * (N+1)
    for i, p1 in enumerate(prime):
        for j, p2 in enumerate(prime):
            if i*j > N:
                break
            if p1 and p2:
                semiprime[i*j] = True
    
    answer = []
    for p, q in zip(P, Q):
        answer.append(sum(semiprime[p:q+1]))
    
    return answer


# 100%
def solution(N, P, Q):
    # semiprime은 prime의 곱으로 만들어진 것들
    prime = [True] * (N+ 1)
    prime[0] = prime[1] = False
    i = 2
    while (i * i <= N):
        if (prime[i]):
            k = i * i
            while (k <= N):
                prime[k] = False
                k += i
        i += 1
    # prime[i]: i가 prime number인지 아닌지

    semiprime = [False] * (N+1)
    for i, p1 in enumerate(prime):
        for j, p2 in enumerate(prime):
            if i*j > N:
                break
            if p1 and p2:
                semiprime[i*j] = True
    
    # 위의 버전 코드에서는 list indexing에서 시간을 꽤 잡아 먹었던 것 같음
    num_semiprime = [0]
    for i in range(1, len(semiprime)):
        num_semiprime.append(num_semiprime[i-1] + semiprime[i])
    
    answer = []
    for p, q in zip(P, Q):
        answer.append(num_semiprime[q] - num_semiprime[p-1])
    
    return answer