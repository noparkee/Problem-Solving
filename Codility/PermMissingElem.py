# Correcteness x
def solution(A):
    A.sort()
    for i in range(len(A)-1):
        if A[i+1] - A[i] != 1:
            return A[i] + 1


# time complexity: O(N ** 2)
def solution(A):
    total = [i for i in range(1, len(A)+2)]
    
    for t in total:
        if not t in A:
            return t


# time complexity: O(N) or O(N * log(N))
def solution(A):    
    A.sort()
    cnt = 1
    answer = 0
    for a in A:
        if a != cnt:
            answer = a - 1
            break
        cnt += 1
    
    if answer == 0:
        answer = len(A) + 1
    
    return answer
