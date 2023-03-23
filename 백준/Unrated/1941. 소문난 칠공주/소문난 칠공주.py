from collections import deque
from itertools import combinations

graph = [list(map(str,input())) for _ in range(5)]
possible = [(i,j) for i in range(5) for j in range(5)]
seats = list(combinations(possible,7))
dx = [0,0,1,-1]
dy = [-1,1,0,0]

def check(arr):
    cnt = 0
    for x,y in arr:
        if graph[x][y] == 'S':
            cnt += 1
    if cnt >= 4:
        return True
    else:
        return False

def solve(arr):
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
                    q.append((nx,ny))
                    visited[idx] = True

    if False in visited:
        return False
    else:
        return True

result = 0
for seat in seats:
    if check(seat):
        if solve(seat):
            result += 1

print(result)