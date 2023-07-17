from collections import deque

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

def solution2(s):
    ans = 0
    que = deque(s)

    for i in range(len(s)):
        check = True
        str = ''.join(que)

        while True:
            if "()" in str:
                str = str.replace("()", "")
            elif "{}" in str:
                str = str.replace("{}", "")
            elif "[]" in str:
                str = str.replace("[]", "")
            elif len(str) != 0:
                check = False
                break
            else:
                break

        if check: ans+=1
        que.rotate(-1)
    return ans

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))
print(solution("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[{{()}}]]]]"))
print('-'*30)
print(solution2("[](){}"))
print(solution2("}]()[{"))
print(solution2("[)(]"))
print(solution2("}}}"))
print(solution2("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[{{()}}]]]]"))