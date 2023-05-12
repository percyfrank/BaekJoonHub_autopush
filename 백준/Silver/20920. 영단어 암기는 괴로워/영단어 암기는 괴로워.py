import sys

n,m = map(int,sys.stdin.readline().split())
words = {}
for _ in range(n):
    tmp = sys.stdin.readline().rstrip()
    if len(tmp) < m:
        continue
    words.setdefault(tmp,0)
    words[tmp] += 1

answer = list(sorted(words.items(),key=lambda x:(-x[1],-len(x[0]),x[0])))

for data in answer:
    print(data[0])