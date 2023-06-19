# 나눴을 때 나머지가 1인 최소값 찾기
def solution(n):
    answer = 0
    if n%2 == 1: return 2

    for i in range(3, n//2 + 1, 2):
        if n%i ==1:
            answer = i
            break

    if answer==0: answer = n-1
    return answer