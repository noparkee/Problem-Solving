# task: 30%, correctness: 57%, performance: 0%
def solution(A, B):
    from math import gcd

    N = max(max(A), max(B))
    prime = [True] * (N+1)
    prime[0], prime[1] = False, False
    i = 2
    while (i*i < N):
        if prime[i]:
            k = i*i
            while k < N:
                prime[k] = False
                k += i
        i += 1
    
    answer = 0
    for a, b in zip(A, B):
        flag = True
        for i in range(2, max(a, b)):
            if prime[i] and a % i == 0 and b % i != 0:
                flag = False
                break
            if prime[i] and a % i != 0 and b % i == 0:
                flag = False
                break
            if prime[i] and max(a, b) % i == 0 and i > min(a, b):
                flag = False
                break
            if not prime[i] and a % i == 0 and b % i == 0:
                break
        if flag:
            answer += 1
            
    return answer


# task: 46%, correctness: 85%, prformance: 0%
def solution(A, B):
    from math import gcd

    N = max(max(A), max(B))
    prime = [True] * (N+1)      # memory error
    prime[0], prime[1] = False, False
    i = 2
    while (i*i < N):
        if prime[i]:
            k = i*i
            while k < N:
                prime[k] = False
                k += i
        i += 1
    
    answer = 0
    for a, b in zip(A, B):
        flag = True
        for i in range(2, max(a, b)+1):
            if prime[i] and a % i == 0 and b % i != 0:
                flag = False
                break
            if prime[i] and a % i != 0 and b % i == 0:
                flag = False
                break
            if prime[i] and max(a, b) % i == 0 and i > min(a, b):
                flag = False
                break
            if not prime[i] and a % i == 0 and b % i == 0:
                break
        if flag:
            answer += 1
            
    return answer


# 100%
# ref: https://sustainable-dev.tistory.com/39
def solution(A, B):
    from math import gcd

    answer = 0
    for a, b in zip(A, B):
        d = gcd(a, b)
        d_a, d_b = 0, 0
        while d_a != 1:
            d_a = gcd(a, d)
            a = a // d_a
        
        while d_b != 1:
            d_b = gcd(b, d)
            b = b // d_b
        
        if a == 1 and b == 1:
            answer += 1

    return answer
