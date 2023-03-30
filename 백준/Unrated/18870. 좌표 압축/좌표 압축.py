n = int(input())
coords = list(map(int,input().split()))
rank = [0 for _ in range(n)]

arr = list(set(coords))
arr.sort()
coord_rank = dict()

for i in range(len(arr)):
    coord_rank[arr[i]] = i

for coord in coords:
    print(coord_rank[coord], end = ' ')