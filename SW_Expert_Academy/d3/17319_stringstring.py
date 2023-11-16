T = int(input())

for t in range(1, 1+T):
    N = int(input())
    S = input()

    if N%2 == 1:
        print('#', t, ' ', 'No', sep='')
        continue

    if S[0:N//2] == S[N//2:N]:
        print('#', t, ' ', 'Yes', sep='')
    else:
        print('#', t, ' ', 'No', sep='')