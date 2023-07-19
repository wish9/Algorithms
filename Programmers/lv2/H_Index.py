def solution2(citations): # 오래 고민했던 잘못된 풀이
    answer = 0
    citations.sort()

    for i in range(len(citations)):
        if citations[i] <= len(citations) - i:
            answer = citations[i]
        else:
            break

    return answer

def solution(citations):
    citations.sort()
    for i in range(len(citations)):
        if citations[i] >= len(citations) - i :
            return len(citations) - i
    return 0

# print(solution([3, 0, 6, 1, 5]))
# print(solution([0, 0, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5,5, 5]))
# print(solution([0, 0, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 10, 10, 10, 3, 3, 3]))
# print(solution([1, 1, 1, 1, 1]))
# print(solution([0, 1, 2, 2, 4]))
# print(solution([0, 1, 2, 3, 4]))
# print(solution([0, 1, 2, 2, 2]))
print(solution([0,5,6,7,8]))
print(solution2([0,5,6,7,8]))
print(solution([3, 4, 4, 4, 5, 5]))
print(solution2([3, 4, 4, 4, 5, 5]))
print(solution([50]))
print(solution2([50]))
print(solution([5, 6, 7]))
print(solution2([5, 6, 7]))
