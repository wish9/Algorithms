import re
from collections import Counter

def solution(str1, str2):
    answer = 0
    arr1 = []
    arr2 = []

    for str in (str1,str2):
        if str == str1: x = arr1
        else: x = arr2
        str = str.upper()

        for i in range(len(str)-1):
            element = str[i] + str[i+1]
            element = re.sub(r"[^a-zA-Z]", "", element)
            if len(element) == 2:
                x.append(element)

    counter1 = Counter(arr1)
    counter2 = Counter(arr2)

    intersection = list((counter1 & counter2).elements())
    union = list((counter1 | counter2).elements())

    if len(union) == 0 & len(intersection) == 0:
        return 65536
    else:
        answer = int(len(intersection)/len(union)*65536)

    return answer

import math

def solution2(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)

print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))
print()
print(solution2("FRANCE", "french"))
print(solution2("handshake", "shake hands"))
print(solution2("aa1+aa2", "AAAA12"))
print(solution2("E=M*C^2", "e=m*c^2"))