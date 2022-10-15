import sys
input = sys.stdin.readline

n = int(input())
meeting = []

for _ in range(n):
    start,end = map(int,input().split())
    meeting.append([start, end])
    
meeting = sorted(meeting, key=lambda a: (a[1],a[0])) 

count = 0
time = 0

for i,j in meeting:
    if i >= time:
        count += 1
        time = j        

print(count)