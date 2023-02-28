def solution(s):
    
    sum = 0
    for alpha in s.upper():
        if(alpha == 'P'):
            sum -= 1
        elif(alpha == 'Y'):
            sum += 1
    
    if(sum == 0): return True
    else: return False
