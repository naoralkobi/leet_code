import copy

board = [[1,2,3],[5,4,0]]


def is_goal(board):
    goal = [[1, 2, 3], [4, 5, 0]]
    for i in range(2):
        if board[i] != goal[i]:
            return False
    return True


def get_empty_box(board):
    for i in range(2):
        for j in range(3):
            if board[i][j] == 0:
                return i, j
    return None


def get_moves(board):
    valid_moves = []
    i, j = get_empty_box(board)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for d in directions:
        temp_board = copy.deepcopy(board)
        new_i = i + d[0]
        new_j = j + d[1]

        if 0 <= new_i <= 1 and 0 <= new_j <= 2:
            temp = temp_board[i][j]
            temp_board[i][j] = temp_board[new_i][new_j]
            temp_board[new_i][new_j] = temp
            valid_moves.append(temp_board)
    return valid_moves


def slidingPuzzle(board):
    queue = [(board, 0)]
    seen = [board]
    while queue:
        current, number = queue.pop(0)
        seen.append(current)
        if is_goal(current):
            return number
        valid_moves = get_moves(current)
        for move in valid_moves:
            if move not in seen:
                queue.append((move, number+1))
    return -1


print(slidingPuzzle(board))

