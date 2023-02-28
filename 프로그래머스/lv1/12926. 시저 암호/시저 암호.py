def solution(s, n):
    
    answer = ''
    
    for a in s:
        if(ord('a') <= ord(a) <= ord('z')):
            answer += chr(ord('a') + (ord(a) + n -ord('a')) % 26)
        elif(ord('A') <= ord(a) <= ord('Z')):
            answer += chr(ord('A') + (ord(a) + n -ord('A')) % 26)
        elif(a == ' '):
            answer += ' '
        
    return answer