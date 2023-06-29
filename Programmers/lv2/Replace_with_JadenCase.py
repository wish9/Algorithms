import re

ip = input()

def solution(s):
    result = ""
    valueList = re.split(r'(\s+)', s)

    for i in range(len(valueList)):
        if valueList[i]:
            result += valueList[i].upper()[0] + valueList[i].lower()[1::]

    return result

print(solution(ip))