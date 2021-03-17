from collections import defaultdict, deque

graph = [[1, 3], [3], [], [2], []]


def dfs_step(g, at, visited):
    visited[at] = True
    print(at, end='->')

    for neibourght in g[at]:
        if neibourght not in visited:
            dfs_step(g, neibourght, visited)


def dfs(g):
    if not g:
        return

    visited = {}

    for v in range(len(g)):
        if v not in visited:
            dfs_step(g, v, visited)


dfs(graph)