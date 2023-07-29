def solution(n):
    answer = []

    def hanoi(original, moveTo, serve, n):
        if n == 1:
            answer.append([original, moveTo])
        else:
            hanoi(original, serve, moveTo, n - 1)
            hanoi(original, moveTo, serve, 1)
            hanoi(serve, moveTo, original, n - 1)

    hanoi(1, 3, 2, n)

    return answer

print(solution(2))
print(solution(3))
print(solution(4))