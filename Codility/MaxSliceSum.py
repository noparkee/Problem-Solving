def solution(A):
    part_max, total_max = 0, 0
    for a in A:
        part_max = max(0, part_max + a)
        total_max = max(part_max, total_max)
    
    return total_max


# correctness 수정
def solution(A):
    part_max, total_max = 0, 0
    for a in A:
        part_max = max(0, part_max + a)
        total_max = max(part_max, total_max)
    
    if total_max == 0 and not 0 in A:
        total_max = max(A)

    return total_max
    