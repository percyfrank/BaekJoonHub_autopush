from collections import deque

def solution(s):

    stack = []
    stack.append(s[0])
    idx = 1
    while idx <= len(s) - 1:
        if not stack:
            stack.append(s[idx])
            idx += 1
            continue
        if stack[-1] == s[idx]:
            stack.pop()
            idx += 1
        else:
            stack.append(s[idx])
            idx += 1
    if not stack:
        return 1
    else:
        return 0
