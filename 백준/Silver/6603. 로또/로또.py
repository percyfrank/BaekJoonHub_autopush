def solve(start):
    if len(answer) == 6:
        print(*answer)
        return

    for i in range(start,len(arr)):
        answer.append(arr[i])
        solve(i+1)
        answer.pop()

while True:
    arr = list(map(int,input().split()))
    if arr[0] == 0:
        break
    arr = arr[1:]
    answer = []
    solve(0)
    print()