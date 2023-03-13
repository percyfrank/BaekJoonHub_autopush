def solution(numbers, target):
    dfs(numbers,0,target,0)
    return answer

answer = 0
def dfs(numbers,idx,target,result):
    global answer
    if idx == len(numbers):
        if result == target:
            answer += 1
            return
    else:
        dfs(numbers,idx+1,target,result+numbers[idx])
        dfs(numbers,idx+1,target,result-numbers[idx])


