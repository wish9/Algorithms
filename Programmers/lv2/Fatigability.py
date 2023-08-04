def explore_dungeons(k, dungeons, fatigue, count):
    # 탐험할 수 있는 던전이 없거나 피로도가 0 이하인 경우
    if not dungeons or fatigue <= 0:
        return count

    max_count = count
    for i in range(len(dungeons)):
        min_fatigue, consume_fatigue = dungeons[i]
        # 해당 던전을 탐험할 수 있는 경우
        if fatigue >= min_fatigue and (fatigue - consume_fatigue) >= 0:
            # 던전을 탐험하고 재귀적으로 다음 던전을 탐험
            new_fatigue = fatigue - consume_fatigue
            max_count = max(max_count, explore_dungeons(k, dungeons[:i] + dungeons[i + 1:], new_fatigue, count + 1))
    return max_count


def solution(k, dungeons):
    return explore_dungeons(k, dungeons, k, 0)


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
print(solution(100, [[90, 50], [50, 20], [50, 10], [50, 40], [10, 10], [20, 10]]))
