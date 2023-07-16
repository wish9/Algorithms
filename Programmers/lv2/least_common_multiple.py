'''
1. 유클리드 호제법을 이용해 최대공약수를 구한다.
2. a,b의 최소공배수 = a*b / 최대공약수
3. 요소 하나씩 포함시켜서 최소공배수를 구한다.
'''
def solution(arr):
    answer = arr[0]

    for i in range(1, len(arr)):
        a = answer
        b = arr[i]
        while b != 0:
            a, b = b, a%b

        answer = answer * arr[i] // a

    return answer

print(solution([2,6,8,14]))
