import sys
input = sys.stdin.readline

def solve(arr):
    q = []
    q.append(arr[0])
    answer = 0
    for i in range(1,20):
        if arr[i] > q[-1]:
            q.append(arr[i])
        else:
            tmp = len(q) - 1
            cnt = 0
            while arr[i] < q[tmp] and tmp >= 0:
                cnt += 1
                tmp -= 1
            q.insert(tmp+1,arr[i])
            answer += cnt
    return answer

p = int(input())
arr = []
for i in range(p):
    arr = list(map(int,input().split()))
    arr = arr[1::]
    print(i+1,solve(arr))