import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))

prefix = [0]
sum = 0
for data in arr:
    sum += data
    prefix.append(sum)

for i in range(m):
    start,end = map(int,input().split())
    print(prefix[end] - prefix[start-1])