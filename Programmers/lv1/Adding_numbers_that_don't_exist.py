ip = list(map(int, input().split()))

def solution(numbers):
    answer = 0
    for i in range(10):
        if not numbers.__contains__(i): answer += i
    return answer

print(solution(ip))