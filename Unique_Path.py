grid = [[1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 2, -1]]


def find_start_position(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                return i, j
    return None


def count_empty_box(grid):
    counter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                counter += 1
    return counter


def uniquePathsIII(grid):
    m, n = len(grid), len(grid[0])
    i, j = find_start_position(grid)
    count = count_empty_box(grid)

    def backtrack(i, j):
        nonlocal count
        result = 0
        for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            # border check
            if 0 <= x < m and 0 <= y < n:
                if grid[x][y] == 0:
                    # traverse down this path
                    grid[x][y] = -1
                    count -= 1
                    result += backtrack(x, y)
                    # backtrack and reset
                    grid[x][y] = 0
                    count += 1
                elif grid[x][y] == 2:
                    # check if all squares have been walked over
                    if count == 0:
                        result += 1
        return result

    return backtrack(i, j)


print(uniquePathsIII(grid))
