def solution(record):
    answer = []
    
    arr = []
    name = {}  
    for data in record:
        arr.append(data.split())

    for data in arr:
        if data[0] == "Enter":
            name[data[1]] = data[2]
            answer.append(data[1] + "님이 들어왔습니다.")
        elif data[0] == "Leave":
            answer.append(data[1] + "님이 나갔습니다.")
        elif data[0] == "Change":
            name[data[1]] = data[2]

    result = []
    for data in answer:
        idx = data.index("님")
        result.append(data.replace(data[:idx],name[data[:idx]]))
    
    return result