def solution(s):

    stack = []
    for alpha in s:
        if not stack:
            stack.append(alpha)
        else:
            if (stack[-1] == alpha):
                stack.pop()
            else:
                stack.append(alpha)
    
    if not stack:
        return 1
    else:
        return 0
