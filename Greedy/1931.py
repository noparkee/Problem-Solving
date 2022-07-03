n = int(input())
meeting = []
num = 0

for i in range(n):
    s, t = map(int, input().split())
    meeting.append((s,t))

meeting.sort(key=lambda x: (x[1], x[0]))

start = meeting[0][0]
for m in meeting:
    if m[0] >= start:
        num += 1
        start = m[1]

print(num)