from collections import deque

def solution(n, wires):
    
    arr = [[] for _ in range(n+1)]
    for a,b in wires:
        arr[a].append(b)
        arr[b].append(a)
    
    def bfs(start):
        visited = [0 for _ in range(n+1)]
        q = deque()
        q.append(start)
        visited[start] = 1
        cnt = 0
        while q:
            node = q.popleft()
            for i in arr[node]:
                if not visited[i]:
                    visited[i] = 1
                    q.append(i)
                    cnt += 1  
        return cnt
    
    answer = n
    for a,b in wires:
        arr[a].remove(b)
        arr[b].remove(a)
        
        answer = min(abs(bfs(a)-bfs(b)),answer)
        
        arr[a].append(b)
        arr[b].append(a)
        
    return answer