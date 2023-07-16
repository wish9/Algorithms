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

'''
문제 내용 중 "테두리 1줄은 갈색" <- 갈색은 한줄뿐이다!!
따라서, 2*(노랑의 가로 + 노랑의 세로) + 4 = 갈색의 총 개수

가로가 세로보다 길어야 하기 때문에
약수들을 찾을 때 0.5제곱근으로 범위 제한하고 해당 약수로 다시 모수를 나눠서 구해지는 대칭 약수를 구할 필요 X
'''
def solution2(brown, yellow):
    for i in range(1, int(yellow**(1/2))+1):
        if yellow % i == 0 and 2*(i + yellow//i) == brown-4:
            return [yellow//i+2, i+2]

print(solution(10,2))
print(solution(8,1))
print(solution(24,24))
print('-'*10)
print(solution2(10,2))
print(solution2(8,1))
print(solution2(24,24))
