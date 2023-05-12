n,x = map(int,input().split())
blogs = list(map(int,input().split()))

prefix = [0]
tmp = 0
for blog in blogs:
    tmp += blog
    prefix.append(tmp)

arr = []
for i in range(x,n+1):
    arr.append(prefix[i] - prefix[i-x])

MAX = max(arr)
cnt = 0
for data in arr:
    if data == MAX:
        cnt += 1

if MAX == 0:
    print("SAD")
else:
    print(MAX)
    print(cnt)