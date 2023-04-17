def solution(str1, str2):
    
    
    list1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    list2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]

    total = set(list1) | set(list2)
    A = 0
    B = 0
    
    if total:
        for words in total:
            A += min(list1.count(words),list2.count(words))
            B += max(list1.count(words),list2.count(words))
        return int(A/B * 65536)
    else:
        return 65536
    
    
