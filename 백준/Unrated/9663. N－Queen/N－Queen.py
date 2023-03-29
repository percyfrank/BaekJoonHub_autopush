n = int(input())

visited1 = [False] * n
visited2 = [False] * (2 * n - 1)
visited3 = [False] * (2 * n - 1)

cnt = 0
def solve(idx):
    global cnt
    if idx == n:
       cnt += 1
       return
    for i in range(n):
        if not visited1[i] and not visited2[idx+i] and not visited3[idx-i+n-1]:
            visited1[i] = True
            visited2[idx+i] = True
            visited3[idx-i+n-1] = True
            solve(idx+1)
            visited1[i] = False
            visited2[idx+i] = False
            visited3[idx-i+n-1] = False

solve(0)
print(cnt)