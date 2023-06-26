ip = int(input())

'''
하샤드 수가 맞는지 판단하는 메서드
* 하샤드 수란 각 자리수 합으로 나누어 떨어지는 수
'''
def solution(n):
    n = str(n)
    sum_each_digit = 0
    for i in range(len(n)):
        sum_each_digit += int(n[i])

    if int(n)%sum_each_digit==0: return True

    return False

def solution2(n):
    return n%sum(int(x) for x in str(n)) == 0

print(solution(ip))
print(solution2(ip))