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
