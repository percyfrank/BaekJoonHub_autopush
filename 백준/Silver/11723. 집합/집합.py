import sys
input = sys.stdin.readline

m = int(input())
s = set()
arr = []

for i in range(m):
    arr = input().split()
    if arr[0] == 'check':
        if int(arr[1]) in s:
            print(1)
        else:
            print(0)
    elif arr[0] == 'add' and int(arr[1]) not in s:
        s.add(int(arr[1]))
    elif arr[0] == 'remove' and int(arr[1]) in s:
        s.remove(int(arr[1]))
    elif arr[0] == 'toggle':
        if int(arr[1]) in s:
            s.remove(int(arr[1]))
        else:
            s.add(int(arr[1]))
    elif arr[0] == 'all':
        s = set([i+1 for i in range(20)])
    elif arr[0] == 'empty':
        s.clear()