a_1, a_0 = map(int, input().split())
c = int(input())
n_0 = int(input())

if (c - a_1) * n_0 >= a_0 and c >= a_1:
    print(1)
else:
    print(0)

# 주의
# c - a_1이 음수일 경우 n_0가 증가함에 따라 값이 감소하무르 c >= a_1 조건이 붙어야 한다.