# 100% 풀긴했는데 뭔가 긴가민가;
def solution(H):
    answer = 0
    stack = []
    for h in H:
        while len(stack) > 0 and stack[-1] > h:
            stack.pop()
        if len(stack) == 0 or stack[-1] < h:
            stack.append(h)
            answer += 1

    return answer


# 다른 풀이 - 이게 이해는 더 잘 됨
# ref: https://velog.io/@jonas-jun/Codility-Wall
def solution(H):
    answer = 0
    stack = []
    for h in H:
        if len(stack) == 0 or h > stack[-1]:
            stack.append(h)
        elif len(stack) > 0 and h < stack[-1]:
            while len(stack) > 0 and h < stack[-1]:
                stack.pop()
                answer += 1
            if len(stack) == 0 or h != stack[-1]:
                stack.append(h)

    answer += len(set(stack))