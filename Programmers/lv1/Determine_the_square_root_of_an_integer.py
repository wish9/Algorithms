ip = int(input())

def solution(n):
    squareRoot = n ** (1/2)

    if squareRoot % 1 == 0:
        return int((squareRoot+1)**2)
    return -1

print(solution(ip))



# print(int(1.5555)) # 소수점이 있는 실수를 int형으로 바꾸면 내림한다.