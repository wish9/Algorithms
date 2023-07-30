def solution(s):
    answer = []
    list_s = [[int(num) for num in i.split(',')] for i in s[2:-2].split("},{")]
    dict_s = {}

    for arr in list_s:
        for item in arr:
            if item not in dict_s:
                dict_s[item] = 1
            else:
                dict_s[item] += 1

    result = sorted(dict_s.items(), key=lambda value: value[1], reverse=True)

    for i in range(len(result)):
        answer.append(result[i][0])

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))