n = int(input())
roads = list(map(int,input().split()))
oils = list(map(int,input().split()))
oils = oils[:n-1]
MIN = min(oils)
answer = 0

if oils[0] == MIN:
    answer = oils[0] * sum(roads)
else:
    answer += oils[0] * roads[0]
    tmp = roads[0]
    for i in range(1,n-1):
        if oils[i] == MIN:
            answer += oils[i] * (sum(roads) - tmp)
            break
        else:
            answer += oils[i] * roads[i]
            tmp += roads[i]

print(answer)