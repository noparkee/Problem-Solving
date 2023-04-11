import itertools

def solution(k, dungeons):
    answer = 0
    num_d = len(dungeons)
    all_path = list(itertools.permutations(dungeons, num_d))

    for a in all_path:
        tmp_k = k
        for i, d in enumerate(a):
            if tmp_k < d[0]:
                if answer < i:
                    answer = i
                break
            else:
                flag = (i == num_d-1)
            tmp_k -= d[1]

        if flag:
            answer = num_d
            break
            
    return answer