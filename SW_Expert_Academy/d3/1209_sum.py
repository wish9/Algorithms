for _ in range(10):
    t = int(input())
    arr = []

    for i in range(100):
        arr.append(list(map(int, input().split())))

    result = []
    for x in arr:
        result.append(sum(x))

    for i in range(100):
        result2 = 0
        for j in range(100):
            result2 += arr[j][i]
        result.append(result2)

    result3 = 0
    result4 = 0

    for diagonal in range(100):
        result3 += arr[diagonal][diagonal]
        result4 += arr[diagonal][99-diagonal]

    result.append(result3)
    result.append(result4)

    print('#', t, ' ', max(result), sep='')