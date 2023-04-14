import itertools
def solution(number):
    answer = 0
    total = list(itertools.combinations(number, 3))
    for t in total:
        if sum(t) == 0:
            answer += 1
    return answer