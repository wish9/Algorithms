T = int(input())

for t in range(1, T + 1):
    values = list(map(int, input().split()))
    print("#%d" % (t), end=' ')
    result = 0

    for i in range(len(values)):
        x = values[i]
        if(x/2!=x//2):
            result += values[i]

    print(result)