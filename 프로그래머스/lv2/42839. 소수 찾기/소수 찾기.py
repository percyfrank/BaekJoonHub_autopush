from itertools import permutations
import math

def isPrime(x):
    
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

def solution(numbers):

    arr = []
    for i in range(len(numbers)):
        arr.append(numbers[i])
    
    result = set()
    
    for length in range(1,len(arr)+1):
        data = list(permutations(arr,length))
        for i in range(len(data)):
            number = int("".join(data[i]))
            if number != 0 and number != 1:
                result.add(number)
    
    answer = 0
    for num in result:
        if isPrime(num):
            answer += 1
    
    return answer