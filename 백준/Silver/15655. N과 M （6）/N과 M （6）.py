def solve(start):
    if len(answer) == m:
        print(*answer)
        return
    for i in range(start,len(arr)):
        if not visited[i]:
            visited[i] = True
            answer.append(arr[i])
            solve(i+1)
            visited[i] = False
            answer.pop()

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
visited = [False] * n
answer = []
solve(0)
