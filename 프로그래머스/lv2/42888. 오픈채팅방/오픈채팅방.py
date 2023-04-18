def solution(record):
    answer = []

    arr = []
    name = {}  
    for data in record:
        if len(data.split()) == 3:
            name[data.split()[1]] = data.split()[2]
            
    for data in record:
        user = data.split()[1]
        if data.split()[0] == "Enter":
            answer.append(name[user] + "님이 들어왔습니다.")
        elif data.split()[0] == "Leave":
            answer.append(name[user] + "님이 나갔습니다.")
    
    return answer
