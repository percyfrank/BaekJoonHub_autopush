from collections import deque

def solution(n, wires):
    
    arr = [[] for _ in range(n+1)]
    for a,b in wires:
        arr[a].append(b)
        arr[b].append(a)
    
    def dfs(start,cnt):
        visited[start] = 1
        for i in arr[start]:
            if not visited[i]:
                cnt = dfs(i,cnt+1)
        return cnt
    
    answer = n
    for a,b in wires:
        arr[a].remove(b)
        arr[b].remove(a)
        
        cnt = 0
        visited = [0 for _ in range(n+1)]
        answer = min(abs(dfs(a,cnt)-dfs(b,cnt)), answer)
        
        arr[a].append(b)
        arr[b].append(a)
        
    return answer