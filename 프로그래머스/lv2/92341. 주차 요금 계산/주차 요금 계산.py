import math

def solution(fees, records):

    arr = []
    for data in records:
        arr.append(data.split(" "))
    
    for i in range(len(arr)):
        h,m = map(int,arr[i][0].split(":"))
        arr[i][0] = h * 60 + m
    
    arr.sort(key=lambda x:(x[1],x[0]))
    
    total = dict()
    flag = True
    for i in range(len(arr)):
        if arr[i][2] == "IN":
            if flag:
                total.setdefault(arr[i][1],0)
                total[arr[i][1]] -= arr[i][0]
                flag = False
            else:
                total.setdefault(arr[i][1],0)
                total[arr[i-1][1]] += 1439
                total[arr[i][1]] -= arr[i][0]
        else:
            total[arr[i][1]] += arr[i][0]
            flag = True
        
    if arr[len(arr)-1][2] == "IN":
        if len(arr) == 1:
            total[arr[len(arr)-1][1]] += 1439 - arr[len(arr)-1][0]
        else:
            total[arr[len(arr)-1][1]] += 1439
            
    answer = []
    for key, value in total.items():
        if value <= fees[0]:
            answer.append(fees[1])
        else:
            minute = math.ceil((value - fees[0]) / fees[2])
            answer.append(fees[1] + minute * fees[3])
            
    return answer