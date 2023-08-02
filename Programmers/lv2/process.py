def solution(priorities, location):
    answer = 0
    pri_que = priorities.copy()
    pri_que.sort(reverse=True)

    while len(priorities) != 0:
        pri_max = pri_que.pop(0)
        max_index = priorities.index(pri_max)
        priorities = priorities[max_index::] + priorities[0:max_index]

        if max_index > location:
            location += len(priorities) - max_index
        else:
            location -= max_index

        if location == 0:
            return answer + 1

        process = priorities.pop(0)
        location -= 1

        if process >= pri_max:
            answer += 1

    return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))