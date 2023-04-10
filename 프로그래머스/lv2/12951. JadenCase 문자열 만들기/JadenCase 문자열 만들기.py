def solution(s):
    
    Jaden = s.split(' ')
    for i in range(len(Jaden)):
    
        Jaden[i] = Jaden[i].capitalize()
        
    return ' '.join(Jaden)
