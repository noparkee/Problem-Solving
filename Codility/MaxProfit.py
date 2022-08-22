# 66% timeout O(N**2)
def solution(A):
    current, max_value = 0, 0
    for i in range(len(A)-1):
        current = -A[i]
        for j in range(i+1, len(A)):
            max_value = max(max_value, current + A[j])
    
    return max_value


#   a를 더해주는 값으로 잡고, min_value를 이동
def solution(A):
    if len(A) < 2:
        return 0

    min_value = A[0]
    profit = 0
    for a in A:
        if profit < a - min_value:
            profit = a - min_value
        if min_value > a:
            min_value = a
    
    return profit
    