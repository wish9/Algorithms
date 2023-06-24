ip = int(input())

def solution(n):
    n = str(n)
    result = ''
    for i in range(9, -1, -1):
        result += str(i)*n.count(str(i))
        n = n.replace(str(i), '')
    return int(result)

def solution2(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))

print(solution(ip))
print(solution2(ip))