n,game = input().split()

player = set()
for _ in range(int(n)):
    player.add(input())

cnt = len(player)
if game == 'Y':
    print(cnt // 1)
elif game == 'F':
    print(cnt // 2)
elif game == 'O':
    print(cnt // 3)