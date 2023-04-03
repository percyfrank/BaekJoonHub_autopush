def isTrianlge(arr):
    if arr[0] + arr[1] <= arr[2]:
        return True

def solve(arr):
    cnt = 0
    for i in range(2):
        if arr[i] == arr[i+1]:
            cnt += 1
    if cnt == 0:
        print('Scalene')
    elif cnt == 1:
        print("Isosceles")
    else:
        print("Equilateral")


while(True):
    arr = list(map(int,input().split()))
    arr.sort()
    cnt = 0
    for data in arr:
        if data == 0:
            cnt += 1
    if cnt == 3:
        break
    if isTrianlge(arr):
        print("Invalid")
        continue
    solve(arr)