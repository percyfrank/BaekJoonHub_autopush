def solution(str1, str2):
    
    answer = 0
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1_j,str2_j = [],[]
    dict_1, dict_2 = dict(), dict()

    
    for i in range(len(str1)-1):
        if 'a' <= str1[i] <= 'z' and 'a' <= str1[i+1] <= 'z':
            str1_j.append(str1[i:i+2])
            dict_1.setdefault(str1[i:i+2],0)
            dict_1[str1[i:i+2]] += 1
    
    for i in range(len(str2)-1):
        if 'a' <= str2[i] <= 'z' and 'a' <= str2[i+1] <= 'z':
            str2_j.append(str2[i:i+2])
            dict_2.setdefault(str2[i:i+2],0)
            dict_2[str2[i:i+2]] += 1

    print(dict_1)
    print(dict_2)
    a = list(set(str1_j) & set(str2_j))
    b = list(set(str1_j) | set(str2_j))
    print("교집합 : ", a)
    print("합집합 : ", b)
    A,B = 0,0
    
    for data in a:
        A += min(dict_1[data],dict_2[data])
        
    for data in b:
        if data in a:
            B += max(dict_1[data],dict_2[data])
        else:
            if data in dict_1:
                B += dict_1[data]
            elif data in dict_2:
                B += dict_2[data]
            
    if A == 0 and B == 0:
        answer = 65536
    else:
        answer = int((A/B) * 65536)

    
    return answer