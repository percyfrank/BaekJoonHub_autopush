def solve(start):
    global cnt
    if sum(answer) == s and len(answer) > 0:
        cnt += 1

    for num in range(start,n):
            answer.append(arr[num])
            solve(num+1)
            answer.pop()

n,s = map(int,input().split())
arr = list(map(int,input().split()))
answer = []
cnt = 0
solve(0)
print(cnt)