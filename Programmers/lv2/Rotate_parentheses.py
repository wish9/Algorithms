def solution(s):
    answer = 0
    openPar = ['(', '{', '[']
    closePar = [')', '}', ']']

    for i in range(len(s)):
        arr = s[i:len(s)] + s[0:i]

        stack = []
        correctPar = True
        for j in arr:
            if openPar.__contains__(j):
                stack.append(j)
            elif closePar.__contains__(j):
                k = closePar.index(j)
                if len(stack) == 0 or stack[-1] != openPar[k]:
                    correctPar = False
                    break
                elif stack[-1] == openPar[k]:
                    stack.pop(-1)
        if correctPar and len(stack)==0:
            answer += 1
    return answer

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))
print(solution("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[{{()}}]]]]"))