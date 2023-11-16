for t in range(1, 11):
    N = int(input())
    hl = list(map(int, input().split()))
    result = 0

    for i in range(2, len(hl)):
        now_h = hl[i]
        near_5_h = hl[i-2:i+3]

        if max(near_5_h) == now_h:
            del near_5_h[2]
            result += now_h - max(near_5_h)

    print('#', t, ' ', result, sep='')