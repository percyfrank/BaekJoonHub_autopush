def solution(msg):
    answer = []
    
    words = {chr(i + 64):i for i in range(1, 27)}
    
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