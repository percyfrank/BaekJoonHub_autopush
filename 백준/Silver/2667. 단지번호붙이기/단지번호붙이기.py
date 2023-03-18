n = int(input())
graph = [list(map(int,input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0

def dfs(x,y):
    if 0 <= x < n and 0 <= y < n and visited[x][y] == 0 and graph[x][y] == 1:
        visited[x][y] = 1
        graph[x][y] = 0
        global cnt
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)
        return True

    return False

arr = []
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and dfs(i,j):
            arr.append(cnt)
        cnt = 0

print(len(arr))
arr.sort()
for num in arr:
    print(num)