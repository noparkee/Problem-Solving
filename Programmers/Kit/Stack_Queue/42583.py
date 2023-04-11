from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    on_bridge = deque([])
    location = deque([])
    
    while truck_weights:
        answer += 1
        
        if len(location) > 0 and location[0] == bridge_length:
            on_bridge.popleft()
            location.popleft()
        
        if (sum(on_bridge) + truck_weights[0] <= weight):
            t = truck_weights.popleft()
            on_bridge.append(t)
            location.append(0)
        
        for i in range(len(location)):
            location[i] += 1
        
    answer += (bridge_length - location[-1])
    
    return answer + 1



### 과거 코드
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = []
    length = []

    l = len(truck_weights)
    while l != 0:
        answer += 1
        
        if length:
            if length[0] == bridge_length:
                length.pop(0)
                bridge.pop(0)
                l -= 1
                
        if truck_weights:
            if truck_weights[0] + sum(bridge) <= weight and len(bridge) < bridge_length:
                bridge.append(truck_weights.pop(0))
                length.append(0)

            for i in range(len(length)):
                length[i] += 1
        
        else:
            answer += (bridge_length - length[-1])
            break
        
            
    return answer