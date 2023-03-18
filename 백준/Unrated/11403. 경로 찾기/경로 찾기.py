from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

a = [[] for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            a[i+1].append(j+1)

def bfs(node):
    q = deque()
    q.append(node)
    while q:
        node = q.popleft()
        for next in a[node]:
            if visited[next] == False:
                visited[next] = True
                q.append(next)

result = [[0] * n for _ in range(n)]

for i in range(1,n+1):
    visited = [False] * (n+1)
    bfs(i)
    for j in range(1,n+1):
        if visited[j] == True:
            result[i-1][j-1] = 1

for i in result:
    print(*i)