def solution(msg):
    
    words = {chr(i + 64):i for i in range(1, 27)}
    
    answer = []
    while True:
        if msg in words:
            answer.append(words[msg])
            break
        for i in range(1,len(msg)+1):
            if msg[0:i] not in words:
                answer.append(words[msg[0:i-1]])
                words[msg[0:i]] = len(words) + 1
                msg = msg[i-1:]
                break
    
    return answer