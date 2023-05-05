def solution(order):
    answer = []
    tmp = []
    idx = 0
    for i in range(1,len(order)+1):
        tmp.append(i)
        while order[idx] == tmp[-1]:
            answer.append(tmp.pop())
            idx += 1
            if not tmp:
                break
    return len(answer)