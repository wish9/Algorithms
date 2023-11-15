T = int(input())

for t in range(1, 1+T):
    N = int(input())
    result = 0

    for i in range(N+1):
        for j in range(1, N+1):
            if i**2 + j**2 <= N**2:
                result +=1

    print('#', t, ' ', result*4+1, sep='')