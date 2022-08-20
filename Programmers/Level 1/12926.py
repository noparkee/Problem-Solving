def solution(s, n):
    answer = ''
    # 65~90: A~Z / 97~122: a~z
    # 알파벳 -> 아스키: ord / 아스키 -> 알파벳: chr
    
    for i in s:
        print(ord(i))
        if i == ' ':
            answer += i
        elif ord(i) + n > 122 and 97 <= ord(i) <= 122:  # 소문자만
            answer += chr(96 + ord(i) + n - 122)
        elif ord(i) + n > 90 and 65 <= ord(i) <= 90:    # 대문자만
            answer += chr(64 + ord(i) + n - 90)
        else:
            answer += chr(ord(i) + n)
        
    return answer