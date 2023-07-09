# n = int(input())
# words = input().strip('[]').replace('"', "").split(', ')

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

def solution2(n, words):
    answer = []
    usedWords = []
    wrongIndex = 0

    for i in range(len(words)):
        now = words[i]
        if i > 0 and (now[0] != words[i-1][-1] or now in usedWords):
            wrongIndex = i
            break
        usedWords.append(now)

    if wrongIndex == 0:
        answer.extend([0, 0])
    else:
        answer.append(wrongIndex % n + 1)
        answer.append(wrongIndex // n + 1)

    return answer


# print(solution(n, words))
# print(solution2(n, words))

print(solution(3 ,["tank", "kick", "know", "wheel", "land",
                   "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either",
                   "recognize", "encourage", "ensure", "establish",
                   "hang", "gather", "refer", "reference", "estimate",
                   "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))