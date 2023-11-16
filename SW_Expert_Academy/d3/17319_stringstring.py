T = int(input())

for t in range(1, 1+T):
    N = int(input())
    S = input()

    if N%2 == 1:
        answer = 'No'
    else:
        if S[0:N//2] == S[N//2:N]:
            answer = 'Yes'
        else:
            answer = 'No'

    print('#', t, ' ', answer, sep='')