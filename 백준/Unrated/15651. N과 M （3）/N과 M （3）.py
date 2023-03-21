def solve(start):
    if len(answer) == m:
        print(*answer)
        return
    for num in range(1,n+1):
        answer.append(num)
        solve(start+1)
        answer.pop()

n,m = map(int,input().split())
visited = [False] *(n+1)
answer = []
solve(1)