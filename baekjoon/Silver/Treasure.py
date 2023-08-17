N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def solution(N, A, B):
    result = 0
    A.sort()
    B.sort(reverse=True)

    for i in range(N):
        result += A[i] * B[i]

    return result

print(solution(N,A,B))