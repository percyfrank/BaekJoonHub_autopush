n = int(input())
dp = [0] * 1000001
dp[1] = 0

for i in range(2,n+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i],dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i],dp[i//3] + 1)

print(dp[n])

num = [n]
def print_num(n):
    if n == 1:
        print(*num)
        return
    elif dp[n] == dp[n-1] + 1:
        num.append(n-1)
        print_num(n-1)
    elif n % 2 ==0  and dp[n] == dp[n//2] + 1:
        num.append(n//2)
        print_num(n//2)
    elif n % 3 == 0 and dp[n] == dp[n//3] + 1:
        num.append(n//3)
        print_num(n//3)

print_num(n)