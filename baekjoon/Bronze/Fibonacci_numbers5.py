ip = int(input())

def fibonacci(n):
    if n == 0: return 0
    elif n == 1 or n == 2: return 1

    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(ip))