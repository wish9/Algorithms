ip = list(map(int, input().split()))

def solution(numbers):
    answer = 0
    for i in range(10):
        if not numbers.__contains__(i): answer += i
    return answer

def solution2(numbers):
    return 45 - sum(numbers)

print(solution(ip))
print(solution2(ip))