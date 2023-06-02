T = int(input())

for t in range(1, T + 1):
    values = list(map(int, input().split()))
    print("#%d" % (t), end=' ')

    le = len(values)
    total = 0
    for i in range(le):
        total += values[i]

    print(round(total/le))