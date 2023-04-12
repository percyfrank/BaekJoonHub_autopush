def solution(arr):
    answer = 0
    
    start = max(arr)
    while True:
        cnt = 0
        for data in arr:
            if start % data == 0:
                cnt += 1
        if cnt == len(arr):
            answer = start
            break
        start += 1
        
                
        
    return answer