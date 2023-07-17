def solution(k, tangerine):
    answer = 0
    tangerine.sort()
    x = tangerine[0]
    i = 1
    count = 1
    result = []

    while True:
        if i == len(tangerine):
            result.append(count)
            break
        elif tangerine[i] == x:
            count += 1
        else:
            result.append(count)
            count = 1
            x = tangerine[i]
        i += 1

    result.sort(reverse=True)
    j = 0
    while k > 0:
        k -= result[j]
        j += 1
        answer += 1

    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))