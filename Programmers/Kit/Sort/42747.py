def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
            
    if n < citations[0]:
        answer = n
    else:
        for i, h in enumerate(citations):
            if n-i <= h:
                answer = n-i
                break
            
    return answer
