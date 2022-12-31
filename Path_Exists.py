import collections

edges = [[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]]
n = 10
source = 7
destination = 5
def validPath(n, edges, source, destination):
    """
    :type n: int
    :type edges: List[List[int]]
    :type source: int
    :type destination: int
    :rtype: bool
    """
    # Store all edges in 'graph'.
    graph = collections.defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    print(graph)

    # Store all the nodes to be visited in 'queue'.
    seen = [False] * n
    seen[source] = True
    queue = collections.deque([source])
    while queue:
        curr_node = queue.popleft()
        if curr_node == destination:
            return True

        # For all the neighbors of the current node, if we haven't visit it before,
        # add it to 'queue' and mark it as visited.
        for next_node in graph[curr_node]:
            if not seen[next_node]:
                seen[next_node] = True
                queue.append(next_node)

    return False


print(validPath(n, edges, source, destination))