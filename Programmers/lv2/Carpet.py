def commonNumbers(n):
    answer = []
    answer.append(1)

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            answer.append(i)
            if n // i != i:
                answer.append(n // i)

    if n != 1:
        answer.append(n)

    return answer

def solution(brown, yellow):
    answer = []
    yellowCommonNumbers = commonNumbers(yellow)

    for i in yellowCommonNumbers:
        transverse = yellow//i+2
        length = i+2
        if transverse*length == brown+yellow and transverse >= length:
            answer.append(transverse)
            answer.append(length)

    return answer


print(solution(10,2))
print(solution(8,1))
print(solution(24,24))
