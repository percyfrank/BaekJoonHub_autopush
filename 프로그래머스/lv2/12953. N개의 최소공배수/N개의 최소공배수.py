# 2개 수의 최소공배수 구하는 함수
def LCM(a, b):
    A, B = a, b
    while b > 0:
        a, b = b, a % b
        
    GCD = a # 최대공약수
    return A * B // GCD

# arr에서 앞 2개씩 접근하면서 최소공배수 갱신
def solution(arr):
    answer = arr[0]
    for i in range(len(arr)-1):
        answer = LCM(answer, arr[i+1])
    return answer