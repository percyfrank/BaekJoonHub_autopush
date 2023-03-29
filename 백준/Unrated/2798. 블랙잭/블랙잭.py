from itertools import combinations

n,m = map(int,input().split())
arr = list(map(int,input().split()))

all = list(combinations(arr,3))
result = 0
for data in all:
     if sum(data) > m:
         continue
     else:
         result = max(result,sum(data))

print(result)