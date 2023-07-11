def sameMach(a,b):
    if a % 2 == 1:
        a += 1
    if b % 2 == 1:
        b += 1
    if a==b:
        return False
    return True

def solution(n, a, b):
    answer = 0

    while sameMach(a,b):

        if a % 2 == 1:
            a = (a + 1) / 2
        else:
            a = a / 2

        if b % 2 == 1:
            b = (b + 1) / 2
        else:
            b = b / 2

        answer += 1

    return answer

print(solution(8,4,7))