def solution(numbers, k):
    answer = 1 + (k - 1) * 2
    return answer%len(numbers) if answer % len(numbers) else len(numbers)

def solution2(numbers, k):
    return (k - 1) * 2 % len(numbers) + 1

print(solution([1, 2, 3, 4], 2))
print(solution([1, 2, 3, 4, 5, 6], 5))
print(solution([1, 2, 3], 3))
print('-'*10)
print(solution2([1, 2, 3, 4], 2))
print(solution2([1, 2, 3, 4, 5, 6], 5))
print(solution2([1, 2, 3], 3))