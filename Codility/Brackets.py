# 75% timeout
def solution(S):
    stack = []
    pair = {")": "(", "]": "[", "}": "{"}
    for s in S:
        if s == "(" or s == "[" or s == "{":
            stack.append(s)
        elif s == ")" or s == "]" or s == "}":
            if len(stack) == 0:
                return 0
            t = stack[-1]
            if t != pair[s]:
                return 0
            stack = stack[:-1]
    
    if len(stack) == 0:
        return 1
    else:
        return 0


# 100 %
# deque 사용
def solution(S):
    from collections import deque
    
    pair = {")": "(", "]": "[", "}": "{"}
    stack = deque([])
    for s in S:
        if s == "(" or s == "[" or s == "{":
            stack.append(s)
        elif s == ")" or s == "]" or s == "}":
            if len(stack) == 0:
                return 0
            t = stack.pop()
            if t != pair[s]:
                return 0
    
    if len(stack) == 0:
        return 1
    else:
        return 0


# pop 사용 (stack = stack[:-1] 보다 pop이 더 빠른 듯)
def solution(S):
    stack = []
    for s in S:
        if s == "(" or s == "[" or s == "{":
            stack.append(s)
        else:
            if len(stack) == 0:
                return 0
            t = stack.pop()
            if s == ")" and t != "(":
                return 0
            elif s == "]" and t != "[":
                return 0
            elif s == "}" and t != "{":
                return 0

    if len(stack) == 0:
        return 1
    else:
        return 0