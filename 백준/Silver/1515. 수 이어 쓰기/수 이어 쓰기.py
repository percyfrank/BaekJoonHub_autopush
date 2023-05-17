num = input()

i = 0
while True:
    i += 1
    start = str(i)

    while len(num) > 0 and len(start) > 0:
        if num[0] == start[0]:
            num = num[1:]
        start = start[1:]

    if len(num) == 0:
        print(i)
        break
