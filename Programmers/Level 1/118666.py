### 2022 KAKAO TECH INTERNSHIP

def solution(survey, choices):
    result_dict = {}
    type = ["R", "T", "C", "F", "J", "M", "A", "N"]
    for t in type:
        result_dict[t] = 0
    
    score = {}
    s = [3, 2, 1, 0, 1, 2, 3]
    for i in range(1, 8):
        if i < 4:
            score[i] = (0, s[i-1])
        else:
            score[i] = (1, s[i-1])
    
    for s, c in zip(survey, choices):
        w = score[c][0]
        result_dict[s[w]] += score[c][1] 
    
    answer = ''
    for i in range(0, len(type), 2):
        if result_dict[type[i]] < result_dict[type[i+1]]:
            answer += type[i+1]
        else:
            answer += type[i]
    
    return answer