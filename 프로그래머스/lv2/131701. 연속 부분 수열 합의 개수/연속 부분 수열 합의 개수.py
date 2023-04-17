def solution(elements):
    
    arr = []
    num = set()
    tmp = elements * 2
    
    for i in range(len(elements)):
        for j in range(len(tmp)-i):
            num.add(sum(tmp[j:j+i]))
        
    return len(num)