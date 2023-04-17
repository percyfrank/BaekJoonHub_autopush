import math

def isPrime(x):
    if x < 2:
        return False
    for i in range(2,int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True


def solution(n, k):
    
    words=""
    while n:           
        words = str(n%k)+words
        n=n//k
    words = words.split('0')  
    
    answer = 0
    for word in words:
        if len(word) == 0:
            continue
        if isPrime(int(word)):
            answer += 1

    return answer