def solve():
    if len(answer) == m:
        print(*answer)
        return
    tmp = 0
    for i in range(len(arr)):
        if tmp != arr[i]:
            answer.append(arr[i])
            tmp = arr[i]
            solve()
            answer.pop()

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
answer = []
solve()