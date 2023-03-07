def solution(number, k):
    
    answer = []
    
    for num in number:
        
        # 스택이 비어있지 않고, 스택의 마지막 값보다 들어올 값이 큰 경우
        while answer and answer[-1] < num and k > 0:
            answer.pop()
            k -= 1
        
        # number를 차례로 넣기
        answer.append(num)
    
    # 다 제거되지 못한 경우(number의 구성이 내림차순으로 계속 이어질때)
    if k > 0:
        answer = answer[:-k]
        
    
    return ''.join(answer)