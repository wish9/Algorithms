def solution(board):
    answer = 0
    len_board = len(board)
    direction = [[0,0], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1,1]]

    for i in range(len_board):
        for j in range(len_board):
            is_bomb = True

            for k in direction:
                if overRange(i+k[0], j+k[1], len_board) and board[i+k[0]][j+k[1]] == 1:
                    is_bomb = False
                    break

            if is_bomb:
                answer += 1

    return answer

def overRange(x,y,arr_len):
    if x < 0 or y < 0 or x >= arr_len or y >= arr_len:
        return False
    return True


print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))
print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))