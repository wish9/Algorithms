def solution(numbers, target):
    def dfs(index, number_sum):
        if index == len(numbers):
            if number_sum == target:
                return 1
            else:
                return 0
        else:
            return dfs(index + 1, number_sum + numbers[index]) + dfs(index + 1, number_sum - numbers[index])

    return dfs(0, 0)

print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))



