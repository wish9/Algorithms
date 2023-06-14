T = int(input())

for t in range(1, T+1):
    N = int(input())
    result = 0
    values = list(map(int, input().split()))
    sellPrice = 0

    for i in values[::-1]:
        if i >= sellPrice:
            sellPrice = i
        else:
            result += sellPrice - i
    print("#", t, " ", result, sep="")