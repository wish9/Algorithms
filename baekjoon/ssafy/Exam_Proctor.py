import math

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

def proctor_division(A, B, C):
    answer = 0

    for candidate_num in A:
        if candidate_num <= B:
            answer += 1
        else:
            answer += math.ceil((candidate_num - B) / C) + 1

    return answer

print(proctor_division(A, B, C))