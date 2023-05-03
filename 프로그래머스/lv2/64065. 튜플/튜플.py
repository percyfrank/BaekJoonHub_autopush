def solution(s):
    answer = []
    
    s = s[2:-2]
    s = s.split('},{')
    s.sort(key=lambda x:len(x))

    for data in s:
        tmp = data.split(',')
        for i in tmp: 
            if int(i) not in answer:
                answer.append(int(i))

    return answer