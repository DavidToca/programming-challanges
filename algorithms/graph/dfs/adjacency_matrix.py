from collections import deque

graph = [
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0],
    [0, 0, 1, 0],
]


def dfs(g):
    if not g:
        return
    visited = {}

    for v in range(len(graph)):
        if v in visited:
            continue
        queue = deque()
        queue.append(v)

        while queue:
            v = queue.popleft()

            if v in visited:
                continue
            visited[v] = True
            print(v, end="->")

            for neigthbour, active in enumerate(g[v]):
                if not active:
                    continue
                if neigthbour not in visited:
                    queue.append(neigthbour)


dfs(graph)