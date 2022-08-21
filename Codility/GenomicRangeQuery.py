# 62 %: time out 
def solution(S, P, Q):
    dna = {"A": 1, "C": 2, "G": 3, "T": 4}
    answer = []
    for p, q in zip(P, Q):
        s = list(S[p:q+1])
        s.sort()
        answer.append(dna[s[0]])

    return answer


# 때로는 노가다가 더 좋다!
def solution(S, P, Q):
    answer = []
    for p, q in zip(P, Q):
        if "A" in S[p:q+1]:
            answer.append(1)
        elif "C" in S[p:q+1]:
            answer.append(2)
        elif "G" in S[p:q+1]:
            answer.append(3)
        elif "T" in S[p:q+1]:
            answer.append(4)
    
    return answer
