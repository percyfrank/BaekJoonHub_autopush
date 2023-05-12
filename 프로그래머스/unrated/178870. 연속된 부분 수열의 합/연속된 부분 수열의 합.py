def solution(sequence, k):
    answer = []
    
    end = 0
    tmp = 0
    
    for start in range(len(sequence)):
        
        while end < len(sequence) and tmp < k:
            tmp += sequence[end]
            end += 1
        
        if tmp == k:
            answer.append([start,end-1])
            
        tmp -= sequence[start]
            
    answer.sort(key=lambda x:(x[1]-x[0]))
    
    return answer[0]