def solve(start):
    if len(answer) == l:
        vo = 0
        co = 0
        for i in range(l):
            if answer[i] in vowel:
                vo += 1
            else:
                co += 1
        if vo >= 1 and co >= 2:
            print(''.join(answer))
            return

    for i in range(start,c):
        if not visited[i]:
            visited[i] = True
            answer.append(arr[i])
            solve(i+1)
            visited[i] = False
            answer.pop()

l,c = map(int,input().split())
vowel = ['a','e','i','o','u']
arr = list(map(str,input().split()))
arr.sort()
visited = [False] * c
answer = []
solve(0)