ip = input()

def toBinary(num):
    result = ''
    digit = 0

    while num / (2**(digit+1)) >= 1:
        digit += 1

    for i in range(digit, -1, -1):
        print(num/(2**i))
        if num/(2**i) >= 1:
            result += '1'
            num = num%(2**i)
        else: result += '0'

    return result

def solution(s):
    answer = []
    numOfZerosRemoved = 0
    numOfConversions = 0
    length = 0

    while s != '1':
        numOfZerosRemoved += s.count('0')
        s = s.replace('0', '')
        length = len(s)
        s = toBinary(length)
        numOfConversions += 1

    answer.append(numOfConversions)
    answer.append(numOfZerosRemoved)

    return answer

print(solution(ip))