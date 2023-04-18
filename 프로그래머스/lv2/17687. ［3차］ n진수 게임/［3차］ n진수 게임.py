def convert(number,n):
    if number == 0:
        return "0"
    numbers = "0123456789ABCDEF"
    nums = ""
    while number > 0:
        a,b = divmod(number,n)
        nums = numbers[b] + nums
        number = a
    return nums

def solution(n, t, m, p):
    answer = ''
    
    nums = ''
    start = 0
    while True:
        num = start
        nums += convert(num,n)
        if len(nums) >= m * t:
            break
        start += 1
    
    for i in range(len(nums)):
        if (i+1) % m == p % m:
            answer += nums[i]    
        if len(answer) == t:
            break

    return answer