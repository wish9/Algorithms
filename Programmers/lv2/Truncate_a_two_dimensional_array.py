def solution(n, left, right):
    arr = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            if j <= i:
                arr.append(i)
            else:
                arr.append(j)
    return arr[left:right+1]

print(solution(3,2,5))