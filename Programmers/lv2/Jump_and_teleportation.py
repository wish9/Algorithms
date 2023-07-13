'''
입력 받은 n 보다 작지만 가장 큰 2의 x승을 구하고
n에다 찾은 값(2의 x승)을 빼는걸 반복해서 몇번 뺀지 리턴하는 메서드
'''
def remove_the_square_power_of_two(n, ans):
    x = 0
    a = 1

    if n ==0:
        return ans

    while True:
        if a <= n:
            x += 1
            a = 2 ** x
        else:
            x -= 1
            break

    ans += 1
    ans = remove_the_square_power_of_two(n - 2**x, ans)

    return ans

def solution(n):
    ans = remove_the_square_power_of_two(n, 0)
    return ans

print(solution(5))
print(solution(6))
print(solution(5000))
