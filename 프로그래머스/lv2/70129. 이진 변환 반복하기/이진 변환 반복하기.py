def solution(s):
    answer = []
    
    cal = 0
    cnt = 0
    while True:
        tmp = 0
        for data in s:
            if data == "0":
                tmp += 1
        cnt += tmp
        len_s = len(s) - tmp
        s  = "1" * len_s

        arr = []
        while len_s > 0:
            arr.append(str(len_s % 2))
            len_s //= 2

        s = ''.join(reversed(arr))
        
        cal += 1
        if s == "1":
            break
        
    answer.append(cal)
    answer.append(cnt)
    return answer