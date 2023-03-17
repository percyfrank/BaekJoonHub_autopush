from collections import deque

n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(len(graph)):
    graph[i].sort()

visited = [False] * (n+1)
def dfs(node):
    visited[node] = True
    print(node, end = ' ')
    for i in graph[node]:
        if not visited[i]:
            dfs(i)

def bfs(node):
    visited[node] = True
    q = deque()
    q.append(node)
    while q:
        node = q.popleft()
        print(node, end = ' ')
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

dfs(v)
print()
visited = [False] * (n+1)
bfs(v)