from collections import deque

def solution(queue1, queue2):

    answer = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    if (sum1+sum2) % 2 == 1:
        return -1
    else:
        if max(queue1+queue2) > (sum1+sum2) // 2:
            return -1
    
    while True:
        
        if sum1 > sum2:
            tmp = queue1.popleft()
            sum2 += tmp
            sum1 -= tmp
            queue2.append(tmp)
            answer += 1
        elif sum1 < sum2:
            tmp = queue2.popleft()
            sum1 += tmp
            sum2 -= tmp
            queue1.append(tmp)
            answer += 1
        else:
            break
        
        if answer == 4 * len(queue1):
            return -1
        
    return answer