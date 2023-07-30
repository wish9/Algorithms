from collections import Counter

def solution(clothes):

    clothes_dict = Counter([item[1] for item in clothes])

    answer = 1
    for num in clothes_dict.values():
        answer *= (num + 1)

    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))