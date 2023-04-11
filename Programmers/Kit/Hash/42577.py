### 시간복잡도 고려하면 아래와 같음
### 사전 순으로 정렬했을 때, 인접한 문자열만 비교하면 됨
def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x: x)

    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
        
    return answer



### 시간복잡도 고려 안 했을 때
def solution(phone_book):
    answer = True

    for p1 in phone_book:
        for p2 in phone_book:
            if p1 != p2 and p1 == p2[:len(p1)]:
                return False
    
    return answer