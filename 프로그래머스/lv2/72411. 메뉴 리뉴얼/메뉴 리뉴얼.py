from itertools import combinations
# from collections import Counter

def solution(orders, course):
    answer = []
    
    total = dict()
    for cnt in course:
        tmp = set()
        for order in orders:
            for data in combinations(order,cnt):
                total.setdefault(''.join(sorted(data)),0)
                total[''.join(sorted(data))] += 1     
    print(total)
            

    arr = [[] for _ in range(len(course))]
    for i in range(len(course)):
        for key,value in total.items():
            if len(key) == course[i] and value > 1:
                arr[i].append([key,value])
    # print(arr)
    
    rank = []
    for i in arr:
        MAX = 0
        for j in range(len(i)):
            MAX = max(MAX,i[j][1])
        rank.append(MAX)
    # print(rank)
    
    for i in range(len(rank)):
        for data in arr[i]:
            for j in range(len(data)):
                if data[1] == rank[i] != 0:
                    answer.append(data[0])
                    
    answer = list(set(answer))
    answer.sort()
    
    return answer
