a, b = map(int, input().split())
def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x + x*i)
    return answer

print(solution(a,b))