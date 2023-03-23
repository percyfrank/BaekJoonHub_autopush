from collections import deque

graph = [list(map(str,input())) for _ in range(5)]
answer = 0
arr = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def check(arr):
    visited = [False] * 7
    q = deque()
    q.append(arr[0])
    visited[0] = True

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx,ny) in arr:
                idx = arr.index((nx,ny))
                if not visited[idx]:
                    visited[idx] = True
                    q.append((nx,ny))

    if False in visited:
        return False
    else:
        return True

possible = [[False] * 5 for _ in range(5)]
def solve(depth, startIdx, cntY):
    global answer

    if cntY >= 4:
        return

    if depth == 7:
        if check(arr):
            answer += 1
        return

    for i in range(startIdx,25):
        x = i // 5
        y = i % 5
        arr.append((x,y))
        possible[x][y] = True
        solve(depth+1, i+1, cntY + (graph[x][y] == 'Y'))
        possible[x][y] = False
        arr.pop()

solve(0,0,0)
print(answer)

