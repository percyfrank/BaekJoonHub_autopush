def solve():
    if len(answer) == m:
        print(*answer)
        return
    for i in range(len(arr)):
        answer.append(arr[i])
        solve()
        answer.pop()

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
answer = []
solve()