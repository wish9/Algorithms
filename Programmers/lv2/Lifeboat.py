def solution(people, limit):
    answer = 0
    not_used = []

    people.sort()

    for i in range(len(people)):
        if people[i] > limit - 40:
            answer += 1
        else:
            not_used.append(people[i])

    i = 0
    j = len(not_used) - 1
    answer_part2 = 0

    while len(not_used) != 0:
        if i == j:
            break

        sum_pair = not_used[i] + not_used[j]

        if sum_pair <= limit:
            answer_part2 += 1
            if i+1!=j:
                i += 1
                j -= 1
            else:
                break
        elif sum_pair > limit:
            j -= 1

    answer_part3 = len(not_used) - answer_part2*2
    answer = answer + answer_part2 + answer_part3

    return answer

def solution2(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer


print(solution2([70, 50, 80, 50], 100))
print(solution2([70, 80, 50], 100))
print(solution2([70, 80, 50, 60, 70, 40, 100, 40, 40, 60, 50], 100))
print(solution2([70, 80, 50, 60, 70, 40, 100, 40, 40, 60, 50, 60, 60, 59, 58, 57, 56], 100))