T = int(input())

for t in range(1, T + 1):
    print('#%d' %t, end=' ')
    countingNumList = [False]*10
    n = int(input())

    for i in range(1, 10**6):
        nowNum = i * n
        digits = [int(digit) for digit in str(nowNum)] # 숫자를 자리수로 분리
        false_index = [index for index in range(len(countingNumList)) if not countingNumList[index]] # 아직 못본 숫자
        # false_index = [index for index, value in enumerate(countingNumList) if not value] # 아직 못본 숫자 2번째 방법

        common = [value for value in digits if value in false_index] # 새로 보게 된 숫자
        for j in common:
            countingNumList[j] = True

        if all(countingNumList):
            print(nowNum)
            break
