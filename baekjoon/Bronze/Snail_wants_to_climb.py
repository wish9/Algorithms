import math
def solution(A,B,V):
    return math.ceil((V - A) / (A - B)) + 1

A, B, V = map(int, input().split())

print(solution(A, B, V))