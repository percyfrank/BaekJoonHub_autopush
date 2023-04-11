def solution(n):
    
    start = n+1
    cnt = bin(n).count('1')

    while True:

        if bin(start).count('1') == cnt:
            return start
            break

        start += 1
