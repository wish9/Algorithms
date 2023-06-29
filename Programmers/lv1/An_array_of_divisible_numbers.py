arr = list(map(int, input().split()))
divisor = int(input())

def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0: answer.append(arr[i])

    answer.sort()
    if len(answer)==0: answer.append(-1)
    return answer

# print(solution(arr, divisor).sort()) # sort는 제자리 메서드라 이런식으로 쓰면 None이 나와버림
print(solution(arr, divisor))