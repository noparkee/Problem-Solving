def solution(s):
    binary, zeros = 0, 0
    while True:
        x = ''
        for i in range(len(s)):
            if s[i] != '0':
                x += s[i]
            else:
                zeros += 1
        s = x

        x = ''
        for i in range(len(s)):
            if 2 ** i > len(s):
                break
            x += str((len(s) & 2**i) >> i)
        binary += 1
        s = x

        if s == '1':
            break
            
    answer = [binary, zeros]
    return answer