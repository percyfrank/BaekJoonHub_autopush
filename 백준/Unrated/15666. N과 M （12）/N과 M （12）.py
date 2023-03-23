def solve(start):
    if len(answer) == m:
        print(*answer)
        return
    tmp = 0
    for i in range(start,len(arr)):
        if tmp != arr[i]:
            answer.append(arr[i])
            tmp = arr[i]
            solve(i)
            answer.pop()

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
answer = []
solve(0)