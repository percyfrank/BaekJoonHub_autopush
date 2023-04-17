def solution(want, number, discount):
    answer = 0
    
    total = dict()
    for i in range(len(discount)-9):
        total = {a:b for a,b in zip(want,number)}
        for j in range(i,i+10):
            if discount[j] in total.keys():
                total[discount[j]] -= 1
        
        cnt = 0
        for value in total.values():
            if value == 0:
                cnt += 1
        if cnt == len(want):
            answer += 1
            
    return answer



