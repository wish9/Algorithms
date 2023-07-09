n = int(input())
words = input().strip('[]').replace('"', "").split(', ')

def solution(n, words):
    answer = []
    usedWords = []
    wrongIndex = 0
    lastChar = words[0][-1]
    usedWords.append(words[0])

    for i in range(1, len(words)):
        now = words[i]
        if now[0] != lastChar or now in usedWords:
            wrongIndex = i
            break
        else:
            usedWords.append(now)
            lastChar = now[-1]

    if wrongIndex ==0:
        answer.append(0)
        answer.append(0)
        return answer

    answer.append(wrongIndex%n+1)
    answer.append(wrongIndex//n + 1)

    return answer

print(solution(n, words))
print(words)