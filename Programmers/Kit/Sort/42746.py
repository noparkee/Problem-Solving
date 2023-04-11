def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: (x*4)[:4], reverse=True)
    
    answer = ''.join(numbers)
    while answer[0] == "0" and len(answer) > 1:
        answer = answer[1:]
        
    return answer