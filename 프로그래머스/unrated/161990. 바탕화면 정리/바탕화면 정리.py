def solution(wallpaper):
    
    x = set()
    y = set()
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                x.add(i)
                x.add(i+1)
                y.add(j)
                y.add(j+1)
    
    answer = [0 for _ in range(4)]
    answer[0] = min(x)
    answer[1] = min(y)
    answer[2] = max(x)
    answer[3] = max(y)
    
    return answer
