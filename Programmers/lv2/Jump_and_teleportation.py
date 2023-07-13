'''
사실상 필요 없었던 방법

입력 받은 n 보다 작지만 가장 큰 2의 x승을 구하고
n에다 찾은 값(2의 x승)을 뺀 값을 리턴하는 메서드
'''
def remove_the_square_power_of_two(n):
    x = 0
    a = 1

    while True:
        if a <= n:
            x += 1
            a = 2 ** x
        else:
            x -= 1
            break

    return n - 2**x

def solution(n):
    ans = 0

    while n!=0:
        if n%2==0:
            n = n/2
        else:
            n = n-1
            ans += 1

    return ans

def solution2(n):
    return bin(n).count('1')

print(solution2(5))
print(solution2(6))
print(solution2(5000))
