# n = int타입

# def solution(n):
#     answer = 0
#
#     for i in range(len(str(n))):
#         answer += int(str(n)[i])
#
#     return answer

def solution(n):
    if n < 10:
        return n

    return n%10 + solution(n//10)