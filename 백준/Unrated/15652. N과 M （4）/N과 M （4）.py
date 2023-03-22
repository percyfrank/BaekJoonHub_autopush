def solve(start):
    if len(answer) == m:
        print(*answer)
        return
    for num in range(start,n+1):
            answer.append(num)
            solve(num)
            answer.pop()

n,m = map(int,input().split())
answer = []
solve(1)