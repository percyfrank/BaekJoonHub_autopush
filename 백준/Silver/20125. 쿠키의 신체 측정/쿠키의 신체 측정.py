n = int(input())
graph = []
for i in range(n):
    graph.append(list(input()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

heart_x = 0
heart_y = 0
for x in range(n):
    for y in range(n):
        if graph[x][y] == '*':
            cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == '*':
                    cnt += 1
            if cnt == 4:
                heart_x = x
                heart_y = y
arm_cnt = []
for i, data in enumerate(graph[heart_x]):
    if data == '*':
        arm_cnt.append(i)

left_arm = heart_y - arm_cnt[0]
right_arm = arm_cnt[-1] - heart_y

waist = []
for i in range(n):
    if graph[i][heart_y] == '*':
        waist.append(i)
waist_cnt = waist[-1] - heart_x

left = []
for i in range(waist[-1]+1,n):
    if graph[i][heart_y-1] == '*':
        left.append(i)
left_leg = left[-1] - left[0] + 1

right = []
for i in range(waist[-1]+1,n):
    if graph[i][heart_y+1] == '*':
        right.append(i)
right_leg = right[-1] - right[0] + 1

print(heart_x+1,heart_y+1)
print(left_arm,right_arm,waist_cnt,left_leg,right_leg)