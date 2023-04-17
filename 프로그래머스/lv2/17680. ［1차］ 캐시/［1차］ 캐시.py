from collections import deque

def solution(cacheSize, cities):
    
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
        
    answer = 0
    cache = deque()
    if cacheSize == 0:
        answer += len(cities) * 5
    else:
        for data in cities:
            if data not in cache: 
                if len(cache) + 1 <= cacheSize:
                    cache.append(data)
                    answer += 5
                else:
                    cache.popleft()
                    cache.append(data)
                    answer += 5
            else:
                cache.remove(data)
                cache.append(data)
                answer += 1

    return answer