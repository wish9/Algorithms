def solution(cacheSize, cities):
    answer = 0
    queue = []

    for i in cities:
        value = i.lower()

        if value in queue:
            answer += 1
            queue.remove(value)
        else:
            answer += 5

        queue.append(value)

        if len(queue) > cacheSize:
            queue.pop(0)

    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))