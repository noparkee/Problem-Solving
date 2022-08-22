# task: 55%,  correctness: 100%, performance: 0%
def solution(A):
    answer = []
    for i in range(len(A)):
        cnt = 0
        for j in range(len(A)):
            if i != j:
                if A[i] % A[j] != 0:
                    cnt += 1
        answer.append(cnt)
    
    return answer
