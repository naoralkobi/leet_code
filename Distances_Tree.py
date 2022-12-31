import collections
edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
n = 6


# find route from i to j.
def get_distance(graph, i):
    result = [0] * n
    seen = []
    # result[i] = 0
    stack = collections.deque()
    new_stack = collections.deque()
    neighbors = graph[i]
    for neighbor in neighbors:
        stack.append(neighbor)
    seen.append(i)
    distance = 1
    while stack:
        current = stack.popleft()
        result[current] = distance
        seen.append(current)
        for neighbor in graph[current]:
            if neighbor in seen:
                continue
            new_stack.append(neighbor)

        if not stack:
            distance += 1
            stack = new_stack
            new_stack = collections.deque()

    sum = 0
    for r in result:
        sum += r
    return sum



def sumOfDistancesInTree(n, edges):
    graph = collections.defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    answer = []
    for i in range(n):
        distance = get_distance(graph, i)
        answer.append(distance)
    return answer


print(sumOfDistancesInTree(6, edges))
