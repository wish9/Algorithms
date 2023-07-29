def solution(s):
    answer = []
    used = {}
    for i in range(len(s)):
        if s[i] in used:
            answer.append(i - used[s[i]])
        else:
            answer.append(-1)
        used[s[i]] = i
    return answer

print(solution("banana"))
print(solution("foobar"))