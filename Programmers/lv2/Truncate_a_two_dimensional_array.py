def fail(n, left, right):
    arr = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            if j <= i:
                arr.append(i)
            else:
                arr.append(j)
    return arr[left:right+1]

def fail2(n, left, right):

    arr = [[0]*n for x in range(n)]

    for i in range(0, n):
        j = i

        while j >= 0:
            arr[i][j] = i + 1
            arr[j][i] = i + 1
            j -= 1

    return sum(arr, [])[left:right+1]

def solution(n, left, right):
    arr = []

    for i in range(left, right+1):
        quotient = i//n + 1
        remainder = i%n + 1

        if quotient >= remainder:
            arr.append(quotient)
        else:
            arr.append(remainder)

    return arr

def solution2(n, left, right):
    answer = []
    for i in range(left,right+1):
        answer.append(max(i//n,i%n)+1)
    return answer

print(solution(3,2,5))
print(solution(4,7,14))

print(solution2(3,2,5))
print(solution2(4,7,14))