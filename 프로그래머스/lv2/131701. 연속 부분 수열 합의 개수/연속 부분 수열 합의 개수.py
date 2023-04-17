def solution(elements):
    
    arr = []
    num = set()
    for i in range(len(elements)):
        tmp = elements.copy()
        for j in range(i):
            tmp.append(elements[j])
        for k in range(len(tmp)-i):
            num.add(sum(tmp[k:k+i]))
        
        
    return len(num)