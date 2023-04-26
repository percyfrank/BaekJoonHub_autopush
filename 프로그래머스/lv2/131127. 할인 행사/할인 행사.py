def solution(want, number, discount):
    answer = 0
    
    cart = dict()
    for i in range(len(want)):
        cart[want[i]] = number[i]
    
    for i in range(len(discount)-9):
        tmp = cart.copy()
        for j in range(i,i+10):
            if discount[j] in tmp.keys():
                tmp[discount[j]] -= 1
        cnt = 0
        for _,value in tmp.items():
            if value == 0:
                cnt += 1
        if cnt == len(want):
            answer += 1
            
    
    
    return answer