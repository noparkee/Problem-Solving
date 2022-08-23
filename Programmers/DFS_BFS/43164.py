def solution(tickets):
    answer = []
    link, visited = {}, {}
    for t in tickets:
        if not t[0] in link:
            link[t[0]] = []
            visited[t[0]] = []
        if not t[1] in link:
            link[t[1]] = []
            visited[t[1]] = []
        link[t[0]].append(t[1])
    for k in list(link.keys()):
        link[k] = sorted(link[k], reverse=True)
    
    stack = ["ICN"]
    while stack:
        node = stack[-1]
        if not link[node]:
            answer.append(stack.pop())
        else:
            stack.append(link[node].pop())
    
    answer.reverse()
    return answer

#print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))                                   # ["ICN","JFK","HND","IAD"]
#print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))   # ["ICN","ATL","ICN","SFO","ATL","SFO"]
#print(solution([["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]))   # ["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"]
#print(solution([["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]]))                     # ["ICN", "A", "C", "A", "B", "D"]
