rooms = [[1,3],[3,0,1],[2],[0]]


def canVisitAllRooms(rooms):
    n = len(rooms)
    visited = [False] * n
    keys = [0]

    while keys:
        current_key = keys.pop()
        for key in rooms[current_key]:
            if visited[key]:
                continue
            keys.append(key)
        visited[current_key] = True

    for visit in visited:
        if visit == False:
            return False

    return True


print(canVisitAllRooms(rooms))



