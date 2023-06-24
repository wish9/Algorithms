ip = int(input())

def solution(n):
    n = str(n)
    result = ''
    for i in range(9, -1, -1):
        result += str(i)*n.count(str(i))
        n = n.replace(str(i), '')
    return int(result)

print(solution(ip))