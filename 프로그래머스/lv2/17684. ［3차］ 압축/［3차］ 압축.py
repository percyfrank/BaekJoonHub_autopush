def solution(msg):
    answer = []
    
    words = dict()    
    words[chr(65)] = 1
    for i in range(1,26):
        words[chr(65+i)] = words[chr(65+i-1)] + 1
    
    idx = 0
    tmp = 0
    start = 26
    while True:
        if msg[idx:tmp+1] in words.keys():
            tmp += 1
        else:
            answer.append(words[msg[idx:tmp]])
            words[msg[idx:tmp+1]] = start + 1
            start += 1
            idx = tmp
            
        if tmp == len(msg):
            answer.append(words[msg[idx:tmp]])
            break

    return answer