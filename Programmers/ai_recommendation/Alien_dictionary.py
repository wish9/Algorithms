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

# 뒤늦게 알았지만 solution2의 경우 오류가 있다.
# dic과 spell 모두 중복된 원소를 갖지 않습니다. << 이게 중복된 알파벳이 없다는 의미는 아니다.
# 따라서 예시케이스 3번에 dmoos 같은 word가 dic에 추가된다면 2를 리턴해야하지만 1을 리턴하기 때문에 완벽한 풀이는 아니다.

print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))
print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))
print(solution(["s", "o", "m", "d"], ["dmoos", "dzx", "smm", "sunmmo", "som"]))
print('-'*30)
print(solution2(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
print(solution2(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))
print(solution2(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))
print(solution2(["s", "o", "m", "d"], ["dmoos", "dzx", "smm", "sunmmo", "som"]))