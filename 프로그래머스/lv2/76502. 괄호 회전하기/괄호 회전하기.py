def solution(s):
    answer = 0
    tmp = s
    a = dict()
    a["["] = "]"
    a["{"] = "}"
    a["("] = ")"
    
    for i in range(len(s)):
        tmp = s[i:] + s[:i]
        stack = []
        flag = True
        
        for data in tmp:
            if data == "[" or data == "{" or data == "(":
                stack.append(data)
            else:
                if stack and data == a[stack[-1]]:
                    stack.pop()
                else:
                    flag = False
        
        if flag:
            if not stack:
                answer += 1
                    
    return answer