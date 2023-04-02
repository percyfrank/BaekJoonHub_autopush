def fibo(n):
    if n < 3:
        return
    for i in range(3,n+1):
        zeros.append(zeros[i-1]+zeros[i-2])
        ones.append(ones[i-1]+ones[i-2])

t = int(input())
for _ in range(t):
    zeros = [1,0,1]
    ones = [0,1,1]
    num = int(input())
    fibo(num)
    print(zeros[num], ones[num])