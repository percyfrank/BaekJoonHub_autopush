def solution(n, arr1, arr2):
    map1 = [[0] * n for _ in range(n)]
    map2 = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            map1[i][n-j-1] = arr1[i] % 2
            map2[i][n-j-1] = arr2[i] % 2
            arr1[i] //= 2
            arr2[i] //= 2
    
    answer = ["" for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if(map1[i][j] == 0 and map2[i][j] == 0):
                answer[i] += " "
            else:
                answer[i] += "#"
        
    
    
    return answer