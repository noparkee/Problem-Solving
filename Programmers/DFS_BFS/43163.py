def solution(begin, target, words):
    answer = 0
    link = {begin: []}
    length = {begin: 1}
    for w in words:
        if not w in link:
            link[w] = []
            length[w] = 1
        cnt = 0
        for k in range(len(w)):
            if begin[k] != w[k]:
                cnt += 1
        if cnt == 1:
            link[begin].append(w)
            link[w].append(begin)
        
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if words[i] != words[j]:
                cnt = 0
                for k in range(len(words[i])):
                    if words[i][k] != words[j][k]:
                        cnt += 1
                if cnt == 1:
                    link[words[i]].append(words[j])
                    link[words[j]].append(words[i])
    
    from collections import deque
    queue, visited = deque([begin]), []
    flag = False
    while queue:
        w = queue.popleft()
        if not w in visited:
            visited.append(w)
            tmp = set(link[w]) - set(visited)
            queue += tmp
            for t in tmp:
                length[t] += length[w]
            if target in queue:
                flag = True
                break
    
    if flag:
        answer = length[target] - 1
        return answer
    else:
        return 0
                

### 다른풀이
def solution(begin, target, words):
    from collections import deque
    answer = 0
    queue = deque([[begin, 0]])
    visited = [0 for _ in range(len(words))]

    while queue:
        w = queue.popleft()
        if w[0] == target:
            return w[1]
        
        for i in range(len(words)):
            cnt = 0
            if visited[i] == 0:
                for j in range(len(words[i])):
                    if words[i][j] != w[0][j]:
                        cnt += 1
                if cnt == 1:
                    queue.append([words[i], w[1]+1])
                    visited[i] = 1
    
    return answer

#print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))   # 4
#print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))          # 0
#print(solution("hit", "cog", ["dot", "dog", "hot", "cog"]))                 # 4
#print(solution("hit", "hhh", ["hhh", "hht"]))                               # 2