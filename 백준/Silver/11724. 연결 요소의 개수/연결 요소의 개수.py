from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(node):
    q = deque()
    q.append(node)
    while q:
        next = q.popleft()
        visited[next] = True
        for i in graph[next]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

cnt = 0
for i in range(1,n+1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)