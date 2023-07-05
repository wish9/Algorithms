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

print(solution(ip))