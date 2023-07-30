from itertools import combinations
import numpy as np

def solution(clothes):
    answer = 0

    from collections import Counter
    clothes_dict = Counter([item[1] for item in clothes])

    arr = clothes_dict.values()

    for r in range(len(arr) + 1):
        for subset in combinations(arr, r):
            answer += np.prod(subset)

    return int(answer) - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))