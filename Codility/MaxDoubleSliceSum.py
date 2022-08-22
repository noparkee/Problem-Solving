# 53% timeout O(N**3)
def solution(A):
    answer = 0 
    for x in range(len(A)-2):
        for y in range(x+1, len(A)-1):
            for z in range(y+1, len(A)):
                answer = max(answer, sum(A[x+1:y]) + sum(A[y+1:z]))
    
    return answer


# ref: https://smecsm.tistory.com/228
# left_sum, right_sum 채우기
# 3개의 index: X, Y, Z에 의해 구간이 나뉘어지고, X, Z에 의해 가장 양끝은 어떤 그룹에도 항상 포함되지 않음
# X, Y, Z에 의해 구간이 나뉘어지지만, X, Z를 0, len(N)-1 으로 고정하고 Y를 움직이며 각 구간에서 ([X+1, Y-1], [Y+1, Z-1]) 최대합을 구하면 됨 (left_sum, right_sum 채우는 과정)
def solution(A):
    left_sum, right_sum = [0] * len(A), [0] * len(A)
    
    for i in range(1, len(A)-1):
        left_sum[i] = max(0, left_sum[i-1] + A[i])
    
    for j in range(len(A)-2, 0, -1):
        right_sum[j] = max(0, right_sum[j+1]+A[j])
    
    answer = 0
    for k in range(len(A)-2):
        answer = max(answer, left_sum[k]+right_sum[k+2])
    
    return answer
