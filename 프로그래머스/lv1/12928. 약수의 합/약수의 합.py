def solution(n):
    
    answer = 0
    common = 1
    
    while common <= n:
        if(n % common == 0):
            answer += common
        common += 1
        
    return answer