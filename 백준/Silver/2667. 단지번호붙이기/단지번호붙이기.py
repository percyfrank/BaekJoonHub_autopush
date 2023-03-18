from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))
visited = [[0] * n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    visited[x][y] = 1
    q = deque()
    q.append((x,y))
    cnt = 1
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    cnt += 1
    return cnt

arr = []
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and graph[i][j] == 1:
            arr.append(bfs(i,j))

print(len(arr))
arr.sort()
for i in arr:
    print(i)