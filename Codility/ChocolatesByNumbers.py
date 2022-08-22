# task: 50%, correctness: 100%, performance: 0% O(N+M)
def solution(N, M):
    chocolate = 0
    ate = [0]
    while True:
        chocolate = (chocolate + M) % N
        if chocolate in ate:
            break
        else:
            ate.append(chocolate)

    return (len(ate))


# 100%
# ref: https://www.youtube.com/watch?v=7F7fICsnNOQ
def solution(N, M):
    from math import gcd
    d = gcd(N, M)
    lcm = (N*M)//d
    return lcm // M