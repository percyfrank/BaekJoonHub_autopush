def solve(depth,n,m):
    if depth == m:
        print(' '.join(map(str,answer)))
        return
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        answer.append(i)
        solve(depth+1,n,m)
        visited[i] = False
        answer.pop()

n,m = map(int,input().split())
visited = [False] * (n+1)
answer = []
solve(0,n,m)