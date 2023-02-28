def solution(participant, completion):
    
    data = dict()
    
    for name in participant:
        data.setdefault(name,0)
        data[name] += 1

    for complete in completion:
        if complete in data.keys():
            data[complete] -= 1
    
    answer = ''      
    for key,value in data.items():
        if (value != 0):
            answer = key
        
    return answer