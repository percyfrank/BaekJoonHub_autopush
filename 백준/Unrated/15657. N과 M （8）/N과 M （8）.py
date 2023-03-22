def solve(start):
    if len(answer) == m:
        print(*answer)
        return
    for i in range(start, len(arr)):
        answer.append(arr[i])
        solve(i)
        answer.pop()

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
answer = []
solve(0)