from collections import deque

def solution(begin, target, words):
    q = deque()
    q.append((begin,0))
    visited = [False] * len(words)
    
    answer = 0
    while q:
        tmp_word, cnt = q.popleft()
        
        if tmp_word == target:
            answer = cnt
            break
        
        for i in range(len(words)):
            tmp = 0
            if not visited[i]:
                for j in range(len(tmp_word)):
                    if tmp_word[j] != words[i][j]:
                        tmp += 1
            if tmp == 1:
                visited[i] = True
                q.append((words[i],cnt+1))
    
    return answer