from collections import Counter

def solution(clothes):

    clothes_dict = Counter([item[1] for item in clothes])

    answer = 1
    for num in clothes_dict.values():
        answer *= (num + 1)

    return answer - 1

def solution2(clothes):
    clothes_type = {}

    for _, item in clothes:
        if item not in clothes_type:
            clothes_type[item] = 2
        else:
            clothes_type[item] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
print()
print(solution2([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution2([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))