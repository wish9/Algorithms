ip = input()

def solution(s):
    valueList = list(map(int, s.split()))
    answer = ("%d %d" %(min(valueList), max(valueList)))
    return answer

print(solution(ip))