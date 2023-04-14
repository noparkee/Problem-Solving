def solution(n, words):
    answer = []
    before_lst = []
    fail, before = None, None
    for i, w in enumerate(words):
        if before:
            if before[-1] != w[0]:
                fail = i+1
                break
        
        if w in before_lst:
            fail = i+1
            break
        
        before = w
        before_lst.append(w)
    
    if fail is None:
        answer = [0, 0]
    else:
        if fail % n == 0:
            answer = [n, fail//n]
        else:
            answer = [fail%n, fail//n + 1]
    
    return answer