def solution(n):
    answer = ''
    regex = "124"
    
    while n > 0:
        n -= 1
        a,b = divmod(n,3)
        answer = regex[b] + answer
        n = a
    return answer