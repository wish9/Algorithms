def solution(wallpaper):
    answer = [float('inf'), float('inf'), -float('inf'), -float('inf')]
    num = 0

    for i in range(len(wallpaper)):
        str = wallpaper[i]
        for j in range(len(str)):
            if str[j] == '#':
                if answer[1] >= j:
                    answer[1] = j
                if answer[0] >= i:
                    answer[0] = i
                if answer[3] <= j+1:
                    answer[3] = j+1
                if answer[2] <= i+1:
                    answer[2] = i+1


    return answer

# print(solution([".#...", "..#..", "...#."]))
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))
