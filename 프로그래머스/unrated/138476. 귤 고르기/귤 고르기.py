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
        k -= a[0][1]
        for i in range(1,len(a)):
            if a[i][1] >= k:
                return i+1
            else:
                k -= a[i][1]
