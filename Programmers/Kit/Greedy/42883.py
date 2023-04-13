def solution(number, k):
    answer = ''
    lst = []
    for i, n in enumerate(number):
        if i == 0:
            lst.append(n)
            continue
        
        while lst:
            if n > lst[-1] and k > 0:
                lst.pop()
                k -= 1
            else:
                break
        lst.append(n)
    
    if k != 0:
        lst = lst[:-k]
    
    answer = ''.join(lst)
    
    return answer