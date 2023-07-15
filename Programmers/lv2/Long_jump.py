import math

'''
순열과 조합을 이용해
2가 한개(i)일 때 n-1(n-i)개의 경우의 수가 발생하는 것을 보고
(n-i)C(i)개의 경우의 수가 발생하고 i는 1부터 n을 2로 나눈 값까지 가능하기에 푼 방법
'''
def solution(n):
    answer = 1
    i_max = n//2

    for i in range(1, i_max+1):
        answer += math.factorial(n-i)//math.factorial(i)//math.factorial(n-2*i) % 1234567

    return answer % 1234567

print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))