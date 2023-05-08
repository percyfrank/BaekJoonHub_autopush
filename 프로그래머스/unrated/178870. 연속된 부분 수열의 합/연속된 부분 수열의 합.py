def solution(sequence, k):
    
    result = []
    
    end = 0
    tmp = 0
    
    for start in range(len(sequence)):
        
        while tmp < k and end < len(sequence) :
            tmp += sequence[end]
            end += 1
            
        if tmp == k:
            result.append([start,end-1])
        
        tmp -= sequence[start]
            
    result.sort(key=lambda x:[(x[1]-x[0]),x[0]])
    
    return result[0]
            