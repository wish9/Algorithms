for t in range(1, 11):
    dum = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    while dum != 0:
        arr[0] += 1
        arr[-1] -= 1
        arr.sort()

        dum -= 1

    print('#', t, ' ', arr[-1] - arr[0], sep='')