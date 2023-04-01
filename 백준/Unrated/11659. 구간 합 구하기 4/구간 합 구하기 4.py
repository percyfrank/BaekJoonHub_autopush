import sys

n,m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

prefix = [0]
sum = 0
for data in arr:
    sum += data
    prefix.append(sum)

for i in range(m):
    start,end = map(int,sys.stdin.readline().split())
    print(prefix[end] - prefix[start-1])