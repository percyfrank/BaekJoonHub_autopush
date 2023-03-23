def solve(start):
    if len(answer) == 6:
        print(*answer)
        return
    for i in range(start, len(arr)):
        if not visited[i]:
            visited[i] = True
            answer.append(arr[i])
            solve(i)
            visited[i] = False
            answer.pop()

while(True):
    arr = list(map(int,input().split()))
    if(arr[0] == 0):
        break
    arr = arr[1:len(arr)]
    visited = [False] * len(arr)
    answer = []
    solve(0)
    print()