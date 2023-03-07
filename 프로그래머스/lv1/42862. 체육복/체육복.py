def solution(n, lost, reserve):
    answer = 0
    
    graph = [True] * (n+1)
    for num in lost:
        if num in reserve:   
            reserve.remove(num)
        else:
            graph[num] = False
        
    lost.sort()
    reserve.sort()
    
    for num in lost:
        if num-1 in reserve:
            graph[num] = True
            reserve.remove(num-1)
            continue
        elif num+1 in reserve:
            graph[num] = True
            reserve.remove(num+1)
            continue
        
    for i in range(1,len(graph)):
        if graph[i]:
            answer += 1
                
    return answer