ip = int(input())

def fibonacci(n):
    if n == 0: return 0
    elif n == 1 or n == 2: return 1

    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(ip))

n = int(input())
dp = [0,1]

for i in range(1,n):
    dp.append(dp[i]+dp[i-1])
print(dp[n])