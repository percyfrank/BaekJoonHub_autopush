from itertools import permutations
import math

def solution(numbers):

    arr = []
    for i in range(len(numbers)):
        arr.append(numbers[i])
    
    result = set()
    
    for length in range(1,len(arr)+1):
        data = list(permutations(arr,length))
        # print(data)
        for i in range(len(data)):
            number = int("".join(data[i]))
            # print(number)
            if number != 0 and number != 1:
                result.add(number)
            
    result = list(result)
    
    for num in range(len(result)):
        for i in range(2,result[num]):
            if result[num] % i == 0:
                result[num] = 0
                break

    answer = 0
    for num in result:
        if num != 0:
            answer += 1
            
    return answer