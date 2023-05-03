from collections import Counter

def solution(topping):
    answer = 0

    a = Counter(topping)
    b = set()
    for i in range(len(topping)):
    
        b.add(topping[i])
        a[topping[i]] -= 1
        
        if a[topping[i]] == 0:
            a.pop(topping[i])
        
        if len(a) == len(b):
            answer += 1
        
    return answer