def solution(arr1, arr2):
    answer = []
    arr2_height = len(arr2)
    arr2_width = len(arr2[0])
    arr1_height = len(arr1)

    i = 0
    j = 0
    k = 0

    arr = []
    result = []

    while i < arr1_height:
        if j < arr2_height:
            arr.append(arr1[i][j] * arr2[j][k])
            j += 1
        else:
            result.append(sum(arr))
            arr = []
            j = 0
            k += 1

        if len(result) == arr2_width:
            answer.append(result)
            i += 1
            k = 0
            result = []

    return answer

def solution2(A, B):
    answer = []

    for i in range(len(A)):
        arr = []
        for j in range(len(B[0])):
            tmp = 0
            for k in range(len(A[0])):
                tmp += A[i][k] * B[k][j]
            arr.append(tmp)
        answer.append(arr)

    return answer

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
# [[15, 15], [15, 15], [15, 15]]
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
# [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4], [5, 1, 6]], [[5, 4, 3, 3], [2, 4, 1, 3], [3, 1, 1, 3]]))
# [[22, 22, 11, 21], [36, 28, 18, 30], [29, 20, 14, 24], [45, 30, 22, 36]]

print(solution2([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution2([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
print(solution2([[2, 3, 2], [4, 2, 4], [3, 1, 4], [5, 1, 6]], [[5, 4, 3, 3], [2, 4, 1, 3], [3, 1, 1, 3]]))