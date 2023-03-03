
def getDivisor(x):
    arr = []
    for i in range(1,x+1):
        if x % i == 0:
            arr.append(i)
    return arr
    
def solution(brown, yellow):
    answer = [0, 0]
    
    arr = getDivisor(yellow)
    for i in range(len(arr)):
        cnt = (arr[i]+arr[len(arr)-i-1])*2 + 4
        if cnt == brown:
            answer[0] = arr[len(arr)-i-1] + 2
            answer[1] = arr[i] + 2
            break

        
    return answer

