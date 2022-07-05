### heapq나 queue의 PriorityQueue를 이용하면 시간초과 해결 (백준에서는 heapq가 PriorityQueue 보단 조금 더 빠른 듯)
import heapq

answer = 0

n = int(input())
card = []

for i in range(n):
    heapq.heappush(card, int(input()))

while len(card) != 1:
    tmp = heapq.heappop(card) + heapq.heappop(card)
    answer += tmp
    heapq.heappush(card, tmp)

print(answer)