def solution(name):
    answer = 0    
    
    data = dict()
    
    for num in range(65,91):
        data[chr(num)] = num
    
    for i in range(len(name)):
        if data[name[i]] - ord('A') <= 13:
            answer += data[name[i]] - ord('A')
        else:
            answer += 90 - data[name[i]] + 1
    
    min_cnt = len(name) - 1
    for i, char in enumerate(name):
        
        next = i+1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        min_cnt = min(min_cnt, 2 * i + len(name)-next, 2*(len(name)-next) + i)
        
    answer += min_cnt
    return answer