def solution(N):
    be_add_tile_quantity = 6
    max_tile_num = 1
    answer = 1

    while N > max_tile_num:
        max_tile_num += be_add_tile_quantity
        answer += 1
        be_add_tile_quantity += 6

    return answer

print(solution(int(input())))