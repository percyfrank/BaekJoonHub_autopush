def solve(start,sum):
    global cnt
    if start >= n:
        return
    sum += arr[start]
    
    if sum == s:
        cnt += 1
    solve(start+1,sum)
    solve(start+1,sum-arr[start])

n,s = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0

solve(0,0)
print(cnt)