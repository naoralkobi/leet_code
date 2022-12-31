def has_route(maze, start, target):
    # for directions.
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    row, col = len(maze), len(maze[0])
    # store the nodes
    stack = []
    seen = set()
    stack.append((start[0], start[1]))
    seen.add((start[0], start[1]))

    while stack:
        cur_i, cur_j = stack.pop()
        for d in directions:
            ni = cur_i
            nj = cur_j
            # rolling loop
            while 0 <= ni <= row and 0 <= nj <= col and maze[ni][nj] == 0:
                ni += d[0]
                nj += d[1]
            ni -= d[0]
            nj -= d[1]
            if ni == target[0] and nj == target[1]:
                return True
            if (ni, nj) not in seen:
                stack.append((ni, nj))
                seen.add((ni, nj))

    return False


def shortest_distance(maze, start, target):
    results = []
    # for directions.
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    row, col = len(maze), len(maze[0])
    steps = 0
    # store the nodes
    stack = []
    seen = set()
    stack.append((start[0], start[1], steps))
    seen.add((start[0], start[1]))

    while stack:
        cur_i, cur_j, temp = stack.pop()

        for d in directions:
            temp_step = temp
            ni = cur_i
            nj = cur_j
            # rolling loop
            while 0 <= ni <= row and 0 <= nj <= col and maze[ni][nj] == 0:
                ni += d[0]
                nj += d[1]
                temp_step += 1
            ni -= d[0]
            nj -= d[1]
            temp_step -= 1
            if ni == target[0] and nj == target[1]:
                results.append(temp_step)
            if (ni, nj) not in seen:
                stack.append((ni, nj, temp_step))
                seen.add((ni, nj))
    if results:
        return min(results)
    return -1


if __name__ == '__main__':

    maze = [[1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 0, 1],
            [1, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1]]

    # need to determine if the ball can hit target.
    # 1. check if there is root to the ball, check if he has wall after.
    result = has_route(maze, [1, 5], [5, 3])
    length = shortest_distance(maze, [1, 5], [5, 3])
    print(result)
    print(length)



