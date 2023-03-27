from collections import deque

graph = [list(map(str,input())) for _ in range(5)]
answer = 0
arr = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 인접 여부 확인
def check(arr):
    visited = [False] * 7
    q = deque()
    q.append(arr[0])
    visited[0] = True
    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx,ny) in arr:
                idx = arr.index((nx,ny))
                if not visited[idx]:
                    q.append((nx,ny))
                    cnt += 1
                    visited[idx] = True

    if cnt != 7:
        return False
    else:
        return True


def solve(startIdx, cntY):
    global answer

    if cntY >= 4:
        return

    if len(arr) == 7:
        if check(arr):
            answer += 1
        return

    for i in range(startIdx,25):
        x = i // 5
        y = i % 5
        arr.append((x,y))
        solve(i+1, cntY + (graph[x][y] == 'Y'))
        arr.pop()

solve(0,0)
print(answer)
