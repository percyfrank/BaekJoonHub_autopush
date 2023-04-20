def solution(numbers):
    
    answer = [-1] * len(numbers)
    stack = []
    
    for index, number in enumerate(numbers):
        while stack and number > numbers[stack[-1]]:
            answer[stack.pop()] = number
        stack.append(index)

    return answer