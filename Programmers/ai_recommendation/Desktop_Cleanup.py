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

def solution2(wall):
    a, b = [], []
    for i in range(len(wall)):
        for j in range(len(wall[i])):
            if wall[i][j] == "#":
                a.append(i)
                b.append(j)
    return [min(a), min(b), max(a) + 1, max(b) + 1]

print(solution([".#...", "..#..", "...#."]))
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))

print(solution2([".#...", "..#..", "...#."]))
print(solution2(["..........", ".....#....", "......##..", "...##.....", "....#....."]))
