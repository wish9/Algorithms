def solution(change):
    coin_types = [25, 10, 5, 1]
    answer = ''
    for coin_type in coin_types:
        quotient = change//coin_type
        answer += str(quotient) + ' '
        change -= quotient * coin_type
    return answer[0:-1:]

for _ in range(int(input())):
    input_value = int(input())
    print(solution(input_value))