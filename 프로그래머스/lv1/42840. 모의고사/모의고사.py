def solution(answers):

    answer = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    records = [0 for _ in range(3)]
    
    for i in range(len(answers)):
        if a[i%5] == answers[i]:
            records[0] += 1
    for i in range(len(answers)):
        if b[i%8] == answers[i]:
            records[1] += 1
    for i in range(len(answers)):
        if c[i%10] == answers[i]:     
            records[2] += 1
        

    for i in range(3):
        if records[i] == max(records):
            answer.append(i+1)
        
    return answer