n = int(input())
m = int(input())

lights = list(map(int,input().split()))

start = 1
end = n

while start <= end:
    mid = (start+end) // 2

    max_area = 0
    flag = True
    for light in lights:
        # 현재 가로등이 비추는 범위가 그 전 가로등이 비추는 최대 범위 보다 작으면
        # 가로등과 가로등 사이의 어두운 곳은 존재하지 않는다.
        if light-mid <= max_area:
            # 현재까지 비추는 최대 범위를 갱신한다.
            max_area = light + mid
        else:
            # i번째 가로등이 비추는 최소 범위가 i-1번째 가로등이 비추는 최대 범위보다 작으면
            # i/i-1번째 가로등 사이의 비추지 못하는 곳이 존재하는 것이므로 바로 종료
            flag = False
            break

    # 마지막 가로등이 비추는 최대 범위가 굴다리의 길이보다 작으면 이것도 다 비추지 못하는 것
    if max_area < n:
        flag = False

    if flag:
        end = mid - 1
    else:
        start = mid + 1

print(start)