def number_of_points_on_side(N):
    if N == 1:
        return 3
    else:
        return number_of_points_on_side(N-1) * 2 - 1
def solution(N):
    return number_of_points_on_side(N) ** 2

print(solution(int(input())))