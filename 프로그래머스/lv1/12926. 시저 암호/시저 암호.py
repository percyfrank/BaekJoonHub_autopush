def solution(s, n):
    
    answer = ''
    
    for a in s:
        if('a' <= a <= 'z'):
            answer += chr(ord('a') + (ord(a) + n - ord('a')) % 26)
        elif('A' <= a <= 'Z'):
            answer += chr(ord('A') + (ord(a) + n - ord('A')) % 26)
        elif(a == ' '):
            answer += ' '
        
    return answer