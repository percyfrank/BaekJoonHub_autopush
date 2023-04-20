def solution(x, y, n):
    
    dp = [float('inf')] * (y+1)
    dp[x] = 0
    
    for i in range(x, y+1):
        if x <= i-n: 
            dp[i] = min(dp[i], dp[i-n]+1)
        if i % 2 == 0 and x <= i//2:
            dp[i] = min(dp[i], dp[i//2]+1)
        if i % 3 == 0 and x <= i//3: 
            dp[i] = min(dp[i], dp[i//3]+1)
            
    if dp[y] == float('inf'):
        return -1
    else:
        return dp[y]
