import sys
sys.setrecursionlimit(10**7)

ip = int(input())

def fibo(n, arr):
    if len(arr) <= n:
        arr.append(fibo(n-1, arr) + fibo(n-2, arr))
    return arr[n] % 1234567

def solution(n):
    if n == 1 or n == 2: return 1
    elif n == 0: return 0
    else:
        arr = [0,1,1]
        return fibo(n, arr)

def solution2(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b%1234567, (a+b)%1234567
    return a

# print(solution(ip)) # 2795 이상부터는 스택 오버플로우 발생
print(solution2(ip))