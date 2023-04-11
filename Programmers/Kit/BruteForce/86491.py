def solution(sizes):
    answer = 0
    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            tmp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = tmp
    
    sizes.sort(key=lambda x: x[0])
    max_w = sizes[-1][0]
    sizes.sort(key=lambda x: x[1])
    max_h = sizes[-1][1]
    
    answer = max_w * max_h
    
    return answer