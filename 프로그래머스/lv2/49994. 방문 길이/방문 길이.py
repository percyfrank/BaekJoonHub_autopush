from collections import deque

def solution(dirs):
    answer = 0
    
    command = {}
    command['U'] = [0,1]
    command['D'] = [0,-1]
    command['R'] = [1,0]
    command['L'] = [-1,0]
    
    arr = set()

    x,y = 0,0
    for dir in dirs:
        nx = x + command[dir][0]
        ny = y + command[dir][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if (nx,ny,x,y) not in arr:
                arr.add((x,y,nx,ny))
            x = nx
            y = ny
    
    return len(arr)