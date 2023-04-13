def solution(s):
    answer = ''
    
    flag = True
    for a in s:
        if a == " ":
            answer += a
            flag = True
            continue

        if flag:
            if 49 <= ord(a) <= 57:
                answer += a
            else:
                answer += a.upper()
            flag = False
        else:
            answer += a.lower()
            
    return answer