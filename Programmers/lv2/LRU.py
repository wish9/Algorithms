def solution(cacheSize, cities):
    answer = 0
    queue = []

    for i in range(len(cities)):
        value = cities[i].upper()

        if queue.__contains__(value):
            answer += 1
        else:
            answer += 5

        queue.append(value)

        if len(queue) > cacheSize:
            queue.pop(0)

    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))