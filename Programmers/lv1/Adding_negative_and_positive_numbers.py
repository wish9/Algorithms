ip1 = list(map(int, input().strip('[]').split(',')))
ip2 = input().strip('[]').split(',')

bool_dict = {'true' or 'True': True, 'false' or 'False': False}
ip2 = [bool_dict[val.lower()] for val in ip2]

def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]: answer += absolutes[i]
        else: answer -= absolutes[i]
    return answer

print(solution(ip1, ip2))