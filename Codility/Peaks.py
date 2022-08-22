# task: 9%, correctness: 16%, performance: 0%
def solution(A):
    peak = []
    for i in range(1, len(A)-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            peak.append(i)
    
    divisor = []
    sqrt = len(A) ** (1/2)
    for i in range(2, int(sqrt)+1):
        if len(A) % i == 0:
            if not i in divisor:
                divisor.append(i)
            if not len(A)//i in divisor:
                divisor.append(len(A)//i)
    divisor.sort(reverse=True)

    answer = 1
    for d in divisor:
        index = [i for i in range(0, len(A), d)]
        cnt = 0
        for i in index:
            tmp = [j for j in range(i, i+d)]
            for p in peak:
                if p in tmp:
                    cnt += 1
                    break
        if cnt == len(index):
            answer += 1

    return answer


# task: 36%, correctness: 50%, performance: 20%
def solution(A):
    peak = [0]
    for i in range(1, len(A)-1):
        if A[i] > A[i+1] and A[i] > A[i-1]:
            peak.append(1)
        else:
            peak.append(0)
    peak.append(0)
    if sum(peak) == 0:
        return 0
    
    divisor = []
    sqrt = len(A) ** (1/2)
    for i in range(2, int(sqrt)+1):
        if len(A) % i == 0:
            if not i in divisor:
                divisor.append(i)
            if not len(A)//i in divisor:
                divisor.append(len(A)//i)
    divisor.sort(reverse=True)

    answer = 1
    for d in divisor:
        start, cnt = 0, 0
        while start < len(A):
            tmp = peak[start:start+d]
            start += d
            if sum(tmp) != 0:
                cnt += 1
        
        if cnt == (len(A) // d):
            answer += 1
    
    return answer


# task: 81%, correctness: 66%, performance: 100%
def solution(A):
    peak = [0]
    for i in range(1, len(A)-1):
        if A[i] > A[i+1] and A[i] > A[i-1]:
            peak.append(1)
        else:
            peak.append(0)
    peak.append(0)
    if sum(peak) == 0:
        return 0

    divisor = []
    sqrt = len(A) ** (1/2)
    for i in range(2, int(sqrt)+1):
        if len(A) % i == 0:
            if not i in divisor:
                divisor.append(i)
            if not len(A)//i in divisor:
                divisor.append(len(A)//i)
    divisor.sort(reverse=True)

    answer = 1
    for d in divisor:
        start, cnt = 0, 0
        while start < len(A):
            tmp = peak[start:start+d]
            start += d
            if sum(tmp) != 0:
                cnt += 1
        
        if cnt == (len(A) // d):
            answer = d
        else:
            break
    
    return answer


# 100%
def solution(A):
    peak = [0]
    for i in range(1, len(A)-1):
        if A[i] > A[i+1] and A[i] > A[i-1]:
            peak.append(1)
        else:
            peak.append(0)
    peak.append(0)
    if sum(peak) == 0:
        return 0

    divisor = []
    sqrt = len(A) ** (1/2)
    for i in range(2, int(sqrt)+1):
        if len(A) % i == 0:
            if not i in divisor:
                divisor.append(i)
            if not len(A)//i in divisor:
                divisor.append(len(A)//i)
    divisor.sort(reverse=True)

    answer = 1
    for d in divisor:
        start, cnt = 0, 0
        while start < len(A):
            tmp = peak[start:start+d]
            start += d
            if sum(tmp) != 0:
                cnt += 1
        
        # 위의 버전에서 break 제거하니까 성공
        if cnt == (len(A) // d):
            answer = len(A) // d
    
    return answer