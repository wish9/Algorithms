def solution(people, limit):
    answer = 0

    while len(people)!=0:
        arr = []
        sum_arr = people[0]
        arr.append(people[0])
        del people[0]

        for i in people:
            if sum_arr < arr[-1] + i <= 100:
                sum_arr = arr[-1] + i
                arr.append(i)

        if len(arr) >= 2:
            people.remove(arr.pop(-1))
            answer += 1
        else:
            answer += 1



    return answer


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
print(solution([70, 19, 80, 50, 30, 50], 100))