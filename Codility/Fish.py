def solution(A, B):
    stack = []
    for a, b in zip(A, B):
        stack.append((a, b))
        while len(stack) > 1 and stack[-1][1] == 0 and stack[-2][1] == 1:
            t1 = stack.pop()
            t2 = stack.pop()
            if t1[0] > t2[0]:
                stack.append(t1)
            else:
                stack.append(t2)

    return len(stack)