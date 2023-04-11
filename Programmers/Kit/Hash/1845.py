def solution(nums):
    answer = 0
    select_num = len(nums) // 2
    
    p = {}
    for n in nums:
        if n not in p:
            p[n] = 1
        else:
            p[n] += 1
    
    unique_id = list(p.keys())
    
    if select_num > len(unique_id):
        answer = len(unique_id)
    else:
        answer = select_num
        
    return answer