def solve():
    if len(answer) == m:
        print(*answer)
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            answer.append(arr[i])
            solve()
            visited[i] = False
            answer.pop()

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
answer = []
visited = [False] * n
solve()