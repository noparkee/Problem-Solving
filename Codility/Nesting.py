def solution(S):
    stack = []
    for s in S:
        if s == "(":
            stack.append(s)
        else:
            if len(stack) == 0:
                return 0
            stack.pop()

    if len(stack) != 0:
        return 0
    else:
        return 1
