T = int(input())

for t in range(1, T + 1):
    inputValues = list(map(int, input().split()))
    print('#%d' % t, end=' ')

    fareA = inputValues[0] * inputValues[4]
    if inputValues[2] >= inputValues[4]:
        fareB = inputValues[1]
    else: fareB = inputValues[1] + (inputValues[4] - inputValues[2]) * inputValues[3]

    if fareA >= fareB:
        print(fareB)
    else: print(fareA)