def solution(n):
    answer = 0
    start = n+1
    
    tmp = []
    while n > 0:
        tmp.append(n % 2)
        n //= 2
    cnt = tmp.count(1)
    
    while True:
        
        ans = start
        arr = []
        while ans > 0:
            arr.append(ans % 2)
            ans //= 2
        
        if arr.count(1) == cnt:
            answer = start
            break
            
        start += 1
    
    return answer