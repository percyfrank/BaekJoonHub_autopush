import math

def to(n,exp):
    regex = "0123456789"
    str = ""
    
    while n > 0:
        a,b = divmod(n,exp)
        str = regex[b] + str
        n = n // exp

    return str

def isPrime(n):
    if n < 2: 
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    num = to(n,k)
    result = num.split('0')
    
    for data in result:
        if data == "":
            continue
        if isPrime(int(data)):
            answer += 1
            
    return answer