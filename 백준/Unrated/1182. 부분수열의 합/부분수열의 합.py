from itertools import combinations

n,s = map(int,input().split())
arr = list(map(int,input().split()))

cnt = 0
for i in range(1,n+1):
    a = list(combinations(arr,i))
    for data in a:
        if sum(data) == s:
            cnt += 1

print(cnt)