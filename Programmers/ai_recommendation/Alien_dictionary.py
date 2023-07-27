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

print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))
print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))