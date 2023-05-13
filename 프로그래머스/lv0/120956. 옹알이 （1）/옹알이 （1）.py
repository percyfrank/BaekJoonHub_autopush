from itertools import permutations

def solution(babbling):
    answer = 0
    word = ['aya','ye','woo','ma']
    
    total = []
    for i in range(1,5):
        total.append(list(permutations(word,i)))
    
    result = []
    for i in range(len(total)):
        for j in range(len(total[i])):
            result.append(''.join(total[i][j]))

    for data in babbling:
        if data in result:
            answer += 1
        
    return answer