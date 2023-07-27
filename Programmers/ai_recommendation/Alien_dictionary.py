def solution(spell, dic):
    answer = 2
    for word in dic:
        counting = [0] * len(spell)
        for char in word:
            if char in spell:
                counting[spell.index(char)] += 1
                if counting[spell.index(char)] >1:
                    break
        if counting.count(1) == len(spell):
            answer = 1
            break

    return answer

def solution2(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s): #차집합 연산!!
            return 1
    return 2

print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))
print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))
print('-'*30)
print(solution2(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
print(solution2(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))
print(solution2(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))
print(solution2(["z", "d", "x"], ["def", "dww", "dzxs", "loveaw"]))