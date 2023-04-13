def solution(people, limit):
    answer = 0
    people.sort()
    n = len(people)
    light, heavy = 0, n-1
    while n > 0:
        if people[light] + people[heavy] <= limit:
            light += 1
            heavy -= 1
            n -= 2
            answer += 1
        else:
            heavy -= 1
            n -= 1
            answer += 1
            
    return answer