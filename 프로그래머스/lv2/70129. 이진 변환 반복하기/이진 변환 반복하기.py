def solution(s):
    answer = []
    
    cal = 0
    cnt = 0
    while s != "1":
        tmp = s.count("0")
        cnt += tmp
        len_s = len(s) - tmp

        arr = []
        while len_s > 0:
            arr.append(str(len_s % 2))
            len_s //= 2

        s = ''.join(reversed(arr))
        
        cal += 1
        
    answer.append(cal)
    answer.append(cnt)
    return answer