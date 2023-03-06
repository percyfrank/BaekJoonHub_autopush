from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    graph = list(permutations(dungeons,len(dungeons)))
    
    for data in graph:
        result = 0
        tmp = k
        for i in range(len(dungeons)):
            if tmp >= data[i][0]:
                tmp -= data[i][1]
                result += 1           
            else:
                break
        answer = max(answer,result)
        
    return answer