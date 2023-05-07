from collections import deque

def solution(queue1, queue2):

    answer = 0
    sum1, sum2 = sum(queue1), sum(queue2)
    target = sum1 + sum2
    queue1, queue2 = deque(queue1), deque(queue2) 
    
    if target % 2 != 0:
        return -1
    else:
        if max(queue1+queue2) > target // 2:
            return -1
    
    while answer < 600000:
        if sum1 == sum2:
            return answer
        elif sum1 > sum2:
            tmp = queue1.popleft()
            sum2 += tmp
            sum1 -= tmp
            queue2.append(tmp)
        elif sum1 < sum2:
            tmp = queue2.popleft()
            sum1 += tmp
            sum2 -= tmp
            queue1.append(tmp)
        answer += 1
    
    return -1
    
#     while True:
#         if sum1 
#         if sum1 > sum2:
            # tmp = queue1.popleft()
            # sum2 += tmp
            # sum1 -= tmp
            # queue2.append(tmp)
            # answer += 1
#         elif sum1 < sum2:
            # tmp = queue2.popleft()
            # sum1 += tmp
            # sum2 -= tmp
            # queue1.append(tmp)
            # answer += 1
#         else:
#             return answer
    