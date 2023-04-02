d = [[0 for _ in range(2)] for _ in range(41)]

d[0][0] = 1
d[1][1] = 1
d[2][0] = 1
d[2][1] = 1

for i in range(3,41):
    d[i][0] = d[i-1][0] + d[i-2][0]
    d[i][1] = d[i-1][1] + d[i-2][1]

t = int(input())
for _ in range(t):
    num = int(input())
    print(d[num][0], d[num][1])