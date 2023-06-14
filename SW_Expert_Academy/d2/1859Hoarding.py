def partialCalculation(list):
    if len(list) == 0: return 0

    maxValue = max(list)
    maxIndex = list.index(maxValue) + 1

    if maxIndex-1==0: return 0

    result = 0
    for i in range(maxIndex):
        result += maxValue - list[i]

    result += partialCalculation(list[maxIndex:len(list)])

    return result

T = int(input())

for t in range(1, T+1):
    print("#%d"%t, end=" ")
    N = int(input())
    values = list(map(int, input().split()))

    print(partialCalculation(values))