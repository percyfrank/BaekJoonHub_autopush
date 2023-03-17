from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    visited[x][y] = 1
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx,ny))

t = int(input())
for _ in range(t):
    m,n,k = map(int,input().split())
    graph = [[0] * n for _ in range(m)]
    for _ in range(k):
        X,Y = map(int,input().split())
        graph[X][Y] = 1
    cnt = 0
    visited = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1 and visited[i][j] == 0:
                bfs(i,j)
                cnt += 1
    print(cnt)