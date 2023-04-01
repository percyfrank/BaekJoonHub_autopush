n = int(input())
s = [0 for _ in range(n+1)]
for i in range(1,n+1):
    s[i] = int(input())
dp = [0 for _ in range(n+1)]

if n <= 2:
    print(sum(s))
    exit()

dp[1] = s[1]
dp[2] = s[2]
dp[3] = s[3]

for i in range(4,n+1):
    dp[i] = min(dp[i-2],dp[i-3]) + s[i]

print(sum(s) - min(dp[n-2],dp[n-1]))