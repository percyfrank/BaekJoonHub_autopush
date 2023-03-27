from collections import deque
                  
def solution(n, computers):
    
    def bfs(node):
        q = deque()
        q.append(node)
        visited[node] = True

        while q:
            x = q.popleft()
            for i in range(n):
                if  computers[x][i] == 1 and not visited[i]:
                    visited[i] = True
                    q.append(i)
                    
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
    
    return answer


        
        