ip = input()

def solution(phone_number):
    if len(phone_number)-4 <0: return 'error'
    answer = "*" * (len(phone_number)-4) + phone_number[-4:]
    return answer

print(solution(ip))