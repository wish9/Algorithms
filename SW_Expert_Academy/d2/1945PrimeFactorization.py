def Square_of_x(x, N):
    result = 0
    if N%x == 0:
        N = N/x
        result += (1 + Square_of_x(x, N))
    return result

T = int(input())

for t in range(1, T+1):
    print("#%d" %t, end=" ")
    N = int(input())

    for i in [2, 3, 5, 7, 11]:
        result = Square_of_x(i, N)
        print(result, end=" ")
    print("")