from collections import deque

def solution(s):
    answer = 0
    original = s
    
    while True:        
        flag = True
        stack = deque([])
        for s_i in s:
            if s_i == '(' or s_i == "{" or s_i == "[":
                stack.append(s_i)
            else:
                if len(stack) > 0:
                    if stack[-1] == '(' and s_i == ')':
                        stack.pop()
                    elif stack[-1] == '{' and s_i == '}':
                        stack.pop()
                    elif stack[-1] == '[' and s_i == ']':
                        stack.pop()
                else:
                    flag = False
                    break
        
        if len(stack) == 0 and flag:
            answer += 1
            
        s = s[1:] + s[0]
        if s == original:
            break
    
            
    return answer