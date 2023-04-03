alpha = [0] * 26

word = input()
word = word.lower()

for i in range(len(word)):
    alpha[ord(word[i])-ord('a')] += 1

MAX = max(alpha)
cnt = 0
for data in alpha:
    if data == MAX:
        cnt += 1

if cnt >= 2:
    print("?")
else:
    for i,word in enumerate(alpha):
        if word == MAX:
            print(chr(97 + i).upper())