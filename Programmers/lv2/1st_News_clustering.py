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

print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))