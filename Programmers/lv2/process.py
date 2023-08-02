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

        priorities.pop(0)
        location -= 1
        answer += 1

    return answer

def solution2(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))

print(solution2([2, 1, 3, 2], 2))
print(solution2([1, 1, 9, 1, 1, 1], 0))