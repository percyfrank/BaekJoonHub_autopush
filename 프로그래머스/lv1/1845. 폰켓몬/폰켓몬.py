def solution(nums):
    
    data = set(nums)
    
    answer = 0
    if(len(data) > len(nums) // 2):
        answer = len(nums) // 2
    else :
        answer = len(data)
    
    return answer