# 88% timeout O(N)
# 도저히 모르겠음ㅠㅠ
def solution(A):
    count, count2 = {}, {}
    for a in A:
        if not a in count:
            count[a] = 1
            count2[a] = 0
        else:
            count[a] += 1

    answer = 0
    for i in range(len(A)-1):
        count2[A[i]] += 1
        count[A[i]] -= 1
        d = max(count, key=count.get)
        d2 = max(count2, key=count2.get)
        if d==d2 and (count[d] > sum(count.values()) / 2) and (count2[d2] > sum(count2.values()) / 2):
            answer += 1

    return answer