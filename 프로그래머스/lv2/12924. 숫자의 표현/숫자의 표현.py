def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        start = i
        sum = 0
        while sum < n:
            sum += start
            start += 1
            if sum == n:
                answer += 1
                break
        
    return answer