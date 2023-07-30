def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9):
        slicing_discount = discount[i:10+i]
        k = 0
        for j in range(len(want)):
            if number[j] <= slicing_discount.count(want[j]):
                k += 1
            else:
                break
        if k == len(want):
            answer += 1
    return answer


def solution2(want, number, discount):
    count = {item: 0 for item in want}

    want_dict = {item: num for item, num in zip(want, number)} # item: num 이  "item, num in zip(want, number)"을 순회하며 값을 받는다.

    n = len(discount)
    answer = 0
    for i in range(n):
        if discount[i] in count:
            count[discount[i]] += 1

        if i >= 9:
            if all(count[item] >= want_dict[item] for item in want):
                answer += 1
                count[discount[i - 9]] -= 1

            if discount[i - 9] in count:
                count[discount[i - 9]] -= 1

    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))
print()
print(solution2(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution2(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))