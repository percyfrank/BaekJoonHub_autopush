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
    for data in arr:
        if data[2] == "IN":
                total.setdefault(data[1],[0,data[2]])
                total[data[1]] = [(total[data[1]][0])-data[0],data[2]]
        else:
            total[data[1]] = [(total[data[1]][0])+data[0],data[2]]
               
    answer = []
    for key,value in total.items():
        if value[1] == "IN":
            total[key][0] += 1439 
        if value[0] <= fees[0]:
            answer.append(fees[1])
        else:
            minute = math.ceil((value[0] - fees[0]) / fees[2])
            answer.append(fees[1] + minute * fees[3])
            
    return answer