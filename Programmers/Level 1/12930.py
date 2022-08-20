def solution(s):
    words = s.split(' ')
    answer = ''
    for i in range(len(words)):
        tmp = ''
        for j in range(len(words[i])):
            if j % 2 == 0:
                tmp += words[i][j].upper()
            else:
                tmp += words[i][j].lower()
        answer += tmp
        answer += " "

    return answer[:-1]