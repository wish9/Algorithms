ip = int(input())

def factorial(N):
    answer = 1
    while N != 0:
        answer *= N
        N -= 1

    return answer

print(factorial(ip))