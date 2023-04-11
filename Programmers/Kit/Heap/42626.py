import heapq

def solution(scoville, K):
    answer = 0
    heap_scoville = []
    for s in scoville:
        heapq.heappush(heap_scoville, s)
    
    while True:
        if heap_scoville[0] >= K:
            break
            
        if len(heap_scoville) < 2:
            answer = -1
            break
            
        if len(heap_scoville) >= 2:
            answer += 1
            a = heapq.heappop(heap_scoville)
            b = heapq.heappop(heap_scoville)
            c = a + b*2
            heapq.heappush(heap_scoville, c)
    
    return answer