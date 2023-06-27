ip1, ip2 = map(int, input().split())

def solution(a, b):
    if a > b:
        x = b
        y = a
    else:
        x = a
        y = b
    answer = 0

    for i in range(x, y + 1):
        answer += i

    return answer

def solution2(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))

print(solution(ip1, ip2))
print(solution2(ip1, ip2))