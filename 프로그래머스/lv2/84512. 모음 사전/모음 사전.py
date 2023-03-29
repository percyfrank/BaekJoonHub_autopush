from itertools import product

def solution(word):
    
    vowel = ['A','E','I','O','U']
    words = []
    
    for i in range(1,6):
        tmp = list(product(vowel,repeat=i))
        for j in range(len(tmp)):
            words.append(''.join(tmp[j]))
    
    words.sort()
                         
    return words.index(word)+1
