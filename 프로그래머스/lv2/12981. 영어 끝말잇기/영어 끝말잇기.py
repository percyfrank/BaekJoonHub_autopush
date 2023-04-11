def solution(n, words):

    answer = []
    arr = []
    
    arr.append(words[0])
    for i in range(len(words)-1):
        if words[i][-1] == words[i+1][0]:
            if words[i+1] in arr:
                answer.append((i+1)%n + 1)
                answer.append((i+1)//n + 1)
                break
            else:
                arr.append(words[i+1])
                
        else:
            answer.append((i+1)%n + 1)
            answer.append((i+1)//n + 1)
            break

    if not answer:
        return [0,0]
    else:
        return answer