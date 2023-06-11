T = int(input())

for t in range(1, T + 1):
    print('#%d' %int(input()), end=' ')
    ip = list(map(int, input().split()))

    y = [0] * 101 # 값의 빈도 수를 체크하기 위한 리스트

    for i in range(len(ip)):
        y[ip[i]] += 1

    reversed_y = y[::-1]
    index = reversed_y.index(max(reversed_y))
    maxValue = 100-index

    print(maxValue)