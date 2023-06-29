ip = list(map(int, input().strip('[]').split(',')))

def solution(arr):
    if arr==[10]: return [-1]
    arr.remove(min(arr))
    return arr

print(solution(ip))