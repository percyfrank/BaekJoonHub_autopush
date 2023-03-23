def solve(start):
    if len(answer) == m:
        print(*answer)
        return
    tmp = 0
    for i in range(start,len(arr)):
        if not visited[i] and tmp != arr[i]:
            visited[i] = True
            answer.append(arr[i])
            tmp = arr[i]
            solve(i)
            visited[i] = False
            answer.pop()

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
visited = [False] * n
answer = []
solve(0)