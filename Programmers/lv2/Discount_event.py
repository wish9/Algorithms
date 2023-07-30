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

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))