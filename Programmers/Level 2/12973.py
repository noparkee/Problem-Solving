from collections import deque
def solution(s):
    string = list(s)
    
    stack = deque([])
    flag = True
    while True:
        for s in string:
            if stack:
                tmp = stack.pop()
                if s == tmp and flag:
                    flag = False
                else:
                    stack.append(tmp)
                    stack.append(s)
            else:
                stack.append(s)
            flag = True

        if string == list(stack):
            return 0
        if len(stack) == 0:
            return 1
        
        string = list(stack)
        stack = deque([])
        