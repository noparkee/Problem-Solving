# 50% timeout N**3
def solution(A):
    min = len(A) * abs(sum(A))
    answer = 0
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            tmp = A[i:j+1]
            candidate = sum(tmp) / len(tmp)
        
            if min > candidate:
                min = candidate
                answer = i
    
    return answer


# 60% timout N**2
def solution(A):
    n = len(A)
    tmp = [0] * (n+1)
    for i in range(n):
        tmp[i+1] = tmp[i] + A[i]
    
    min = 100000
    answer = 0
    for p in range(0, n-1):
        for q in range(p+1, n):
            candidate = (tmp[q+1] - tmp[p]) / (q-p+1)
            if candidate < min:
                min = candidate
                answer = p
    
    return answer


# 구글링: 리스트 요소가 2개 혹은 3개일 때 최솟값을 가지게 된다. 요소가 4개 이상일 때는 최솟값을 가질 확률이 x
# ref: https://davi06000.tistory.com/58
def solution(A):
    min = (A[0]+A[1])/2
    answer = 0
    for i in range(0, len(A)-1):
        candidate = (A[i]+A[i+1])/2
        if min > candidate :
            min = candidate
            answer = i

    for j in range(0, len(A)-2):
        candidate = (A[j]+A[j+1]+A[j+2])/3
        if min > candidate :
            min = candidate
            answer = j
    return answer
    