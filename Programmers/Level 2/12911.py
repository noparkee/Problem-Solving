def solution(n):
    answer = ''
    one = 0
    
    binary = str(bin(n))[2:]
    for b in binary:
        if b == '1':
            one += 1

    if one == len(binary):
        answer += '10'
        answer += '1' * (one-1)
    else:
        binary = list(binary)
        fix = 0
        changed = False

        for i in range(len(binary)-1):
            if binary[-i-1] == '1' and binary[-i-2] == '0':
                binary[-i-1] = '0'
                binary[-i-2] = '1'
                fix = -i
                changed = True
                break
        
        if not changed:
            answer = '1'
            answer += '0' * (len(binary)-one+1) + '1'*(one-1)
        
        else:
            one = 0
            tmp = binary[fix:]
            if len(tmp) != len(binary):
                for i in range(len(tmp)):
                    if tmp[fix:][i] == '1':
                        one += 1
                answer += '0' * (len(tmp) - one)
                answer += '1' * one
                answer = ''.join(binary[:fix]) + answer
            else:
                answer = ''.join(binary)
        
    answer = int(answer, 2)
    return answer