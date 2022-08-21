# 62% timoue O(N**2)
def solution(A):
    circle = []
    for i in range(len(A)):
        circle.append((i-A[i], i+A[i]))
    circle.sort()
    
    answer = 0
    for i in range(len(circle)-1):
        for j in range(i+1, len(circle)):
            if circle[i][1] >= circle[j][0]:
                answer += 1
            else:
                break
    
    return answer


# 100%
# left, right를 구분해서 따로 넣어주기
# ref: https://juran-devblog.tistory.com/198?category=865986
def solution(A):
    circle = []
    for i in range(len(A)):
        circle.append((i-A[i], -1))
        circle.append((i+A[i], 1))
    circle.sort()
    
    answer, cnt = 0, 0
    for c in circle:
        if c[1] == 1:
            cnt -=1
        else:
            answer += cnt
            cnt += 1
    if answer > 10000000:
        return -1
    return answer