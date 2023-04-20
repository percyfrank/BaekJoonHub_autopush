def solution(files):

    arr = []
    for data in files:
        head,number,tail = '','',''
        for i in range(len(data)):
            if data[i].isdigit():
                number = data[i:]
                head = data[:i]
                break
        for j in range(len(number)):
            if not number[j].isdigit():
                tail = number[j:]
                number = number[:j]
                break
        arr.append([head,number,tail])
    arr.sort(key=lambda x:(x[0].lower(),int(x[1])))
    
    answer = []
    for data in arr:
        answer.append(''.join(data))
        
    return answer