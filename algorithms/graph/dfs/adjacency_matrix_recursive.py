graph = [
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0],
    [0, 0, 1, 0],
]


def dfs_step(graph, at, visited):
    if at in visited:
        return
    visited[at] = True
    print(at, end='->')
    for neigthbour, active in enumerate(graph[at]):
        if not active:
            continue
        dfs_step(graph, neigthbour, visited)


def dfs(graph):
    visited = {}

    for v in range(len(graph)):
        dfs_step(graph, v, visited)


dfs(graph)