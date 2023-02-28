def solution(id_list, report, k):
    
    tmp = list(set(report))
    # tmp = list(tmp)
    
    graph = {}
    for id in id_list:
        graph[id] = []
    
    data = dict()
    
    for i in range(len(tmp)):
        user = tmp[i].split(' ')[0]
        record = tmp[i].split(' ')[1]
        data.setdefault(record,0)
        data[record] += 1
        graph[user].append(record)
    # print(data)


    idx = dict()

    for key,value in data.items():
        for gkey in graph.keys():
            if value >= k and key in graph[gkey]:
                idx.setdefault(gkey,0)
                idx[gkey] += 1

    print(idx)
    
    answer = [0 for _ in range(len(id_list))]
    for i in range(len(id_list)):
        for key,value in idx.items():
            if key == id_list[i]:
                answer[i] = value
            
    return answer