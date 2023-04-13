def solution(k, tangerine):
    
    a = dict()
    
    for data in tangerine:
        a.setdefault(data,0)
        a[data] += 1 
        
    a = sorted(a.items(),key=lambda x:-x[1])
    
    sum = 0
    answer = 1
    if a[0][1] >= k:
        return 1
    else:
        for data in a:
            if data[1] < k:
                k -= data[1]
                answer += 1
            else:
                break
                        
    return answer   