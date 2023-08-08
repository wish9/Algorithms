import math

N, B = map(int, input().split(" "))

def solution(N, B):
    result = ''
    if N == 0:
        return '0'
    max_conversion_value = int(math.log(N, B))

    for i in range(max_conversion_value, -1, -1):
        value = N//(B**i)
        N -= value * B**i
        if value >= 10:
            value = chr(value+55)
        else:
            value = str(value)

        result += value

    return result

print(solution(60466175, 36))
print(solution(4, 2))
print(solution(N, B))

# 두번째 풀이
# 오차범위 내지만 8ms 더 빠름
# 기능분리가 더 잘됨
n, b = map(int, input().split())


def change(num):
    if num < 10:
        return str(num)
    return str(chr(num + 55))

result = ""

while n >= b:
    n, r = n // b, n % b
    result += str(change(r))
result += str(change(n))
print(result[::-1])