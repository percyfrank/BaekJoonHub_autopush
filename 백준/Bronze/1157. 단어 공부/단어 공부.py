word = input().upper()
cnt = list(set(word))

alpha = []
for data in cnt:
    alpha.append(word.count(data))

if alpha.count(max(alpha)) >= 2:
    print("?")
else:
    print(cnt[alpha.index(max(alpha))])