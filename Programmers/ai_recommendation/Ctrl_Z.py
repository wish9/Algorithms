def solution(s):
    answer = 0
    arr = list(s.split())

    for i in range(len(arr)):
        if arr[i] == "Z":
            answer -= int(arr[i-1])
        else:
            answer += int(arr[i])

    return answer

print(solution("1 2 Z 3"))