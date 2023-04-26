def solution(str1, str2):
    
    arr1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()] 
    arr2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]

    s1 = set(arr1) & set(arr2)
    s2 = set(arr1) | set(arr2)

    a,b = 0,0
    for data in s1:
        a += min(arr1.count(data),arr2.count(data))
    for data in s2:
        b += max(arr1.count(data),arr2.count(data))
        
    if a == b == 0:
        return 65536
    
    return int((a/b) * 65536)
