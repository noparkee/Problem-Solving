s = input()

answer = [0, 0]
answer[int(s[0])] += 1

for i in range(1, len(s)):
    if s[i-1] != s[i]:
        answer[int(s[i])] += 1

print(min(answer))