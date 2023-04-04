n,k = map(int,input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

arr.sort(key=lambda x:(-x[1],-x[2],-x[3]))

rank = dict()
cnt = 1
rank[arr[0][0]] = 1
for i in range(n-1):
    if arr[i][1:3] != arr[i+1][1:3]:
        rank.setdefault(arr[i+1][0],rank[arr[i][0]]+cnt)
    else:
       cnt += 1
       rank[arr[i+1][0]] = rank[arr[i][0]]
        
print(rank[k])