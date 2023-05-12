n = int(input())
arr = list(map(int,input().split()))
arr.sort()
total = int(input())
tmp = 0
answer = 0
start = total // n
end = arr[-1]

while start <= end:
    mid = (start+end) // 2
    tmp = 0
    for data in arr:
        if data < mid:
            tmp += data
        else:
            tmp += mid
    if tmp > total:
        end = mid - 1
    elif tmp < total:
        start = mid + 1
        answer = max(answer,mid)
    else:
        answer = mid
        break
print(answer)