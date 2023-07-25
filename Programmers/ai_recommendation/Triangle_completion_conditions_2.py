
# 삼각형 세 변의 길이를 i, j, x라 하고 i = 아는 길이 중 작은 길이, j = 아는 길이 중 긴 길이, 모르는 값이 x라 하자.
#
# if x가 최대라면?
# x가 가능한 범위는 다음과 같다. i + j > x >= j
# 따라서 i개의 경우의 수 만큼 가능
#
# if j가 최대라면?
# j >= x > j - i
# 따라서 i개의 경우의 수가 가능하지만 x가 최대일 경우 x == j인 경우의 수가 중복되기 때문에 최종결과에는 -1을 해줘야 한다.
#
# 따라서 총 가능한 경우의 수 = 입력 받은 가장 작은 수 * 2 -1

def solution(sides):
    sides.sort()
    return (2*sides[0]-1)

print(solution([1, 2]))
print(solution([3, 6]))
print(solution([11, 7]))