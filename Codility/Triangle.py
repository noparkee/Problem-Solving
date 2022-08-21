# A를 정렬했으니까 A[i] + A[i+1] > A[i+2] 를 만족하면 다른 조건도 만족될 수 밖에 없음
def solution(A):
    answer = 0
    for i in range(len(A)-2):
        if A[i] + A[i+1] > A[i+2]:
            answer = 1
            break
    
    return answer
