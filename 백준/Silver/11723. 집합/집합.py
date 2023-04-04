import sys
input = sys.stdin.readline

m = int(input())
s = set()
arr = []

for i in range(m):
    arr = input().split()
    if len(arr) == 2:
        arr[1] = int(arr[1])
    if arr[0] == 'check':
        if arr[1] in s:
            print(1)
        else:
            print(0)
    elif arr[0] == 'add':
        s.add(arr[1])
    elif arr[0] == 'remove' and arr[1] in s:
        s.remove(arr[1])
    elif arr[0] == 'toggle':
        if arr[1] in s:
            s.remove(arr[1])
        else:
            s.add(arr[1])
    elif arr[0] == 'all':
        s = set([i+1 for i in range(20)])
    elif arr[0] == 'empty':
        s.clear()