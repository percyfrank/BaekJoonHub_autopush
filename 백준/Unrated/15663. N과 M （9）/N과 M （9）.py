def solve():
    if len(answer) == m:
        print(*answer)
        return
    tmp = 0
    for i in range(len(arr)):
        if not visited[i] and arr[i] != tmp:
            visited[i] = True
            answer.append(arr[i])
            tmp = arr[i]
            solve()
            visited[i] = False
            answer.pop()

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
visited = [False] * n
answer = []
solve()