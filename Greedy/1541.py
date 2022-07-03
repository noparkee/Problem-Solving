s = input().split('-')

for i in range(len(s)):
    s[i] = sum(list(map(int, s[i].split('+'))))

answer = s[0]
for i in range(1, len(s)):
    answer -= s[i]

print(answer)