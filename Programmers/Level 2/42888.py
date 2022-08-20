def solution(record):
    record = list(map(lambda x: x.split(), record))

    name_dict = {}
    for r in record:
        if r[0] == "Enter" or r[0] == "Change":
            name_dict[r[1]] = r[2]

            answer = []
    for r in record:
        if r[0] == "Enter":
            answer.append(f"{name_dict[r[1]]}님이 들어왔습니다.")
        elif r[0] == "Leave":
            answer.append(f"{name_dict[r[1]]}님이 나갔습니다.")
    
    return answer