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
    
    return [min(x), min(y), max(x), max(y)]
