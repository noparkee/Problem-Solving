def solution(orders, course):
    from itertools import combinations
    orders = list(map(lambda x: list(x), orders))
    
    answer = []
    for c in course:
        combi = []
        for order in orders:
            combi.append(list(combinations(order, c)))
        flat_lst = [sorted(list(sub_c)) for c in combi for sub_c in c]      # tip: list flat
        candidate = {}
        for f in flat_lst:
            if not ''.join(f) in candidate:
                candidate[''.join(f)] = 1
            else:
                candidate[''.join(f)] += 1
        
        if len(candidate) != 0:
            candidate = sorted(candidate.items(), key=lambda x: (-x[1], x[0]))
            max = candidate[0][1]
            for c in candidate:
                if c[1] >= 2 and c[1] >= max:
                    answer.append(c[0])
    
    answer.sort()
    
    return answer