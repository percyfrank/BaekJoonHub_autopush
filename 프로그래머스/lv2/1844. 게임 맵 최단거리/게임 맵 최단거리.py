from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = 0
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    def bfs(x,y):
        nonlocal answer
        visited = [[False] * m for _ in range(n)]
        q = deque()
        q.append((x,y))
        visited[x][y] = True    
        
        while q:
            x,y = q.popleft()
            print(x,y)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] == 1 and not visited[nx][ny]:
                        maps[nx][ny] = maps[x][y] + 1
                        visited[nx][ny] = True
                        q.append((nx,ny))
                    
    
    bfs(0,0)
    
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]
