from collections import defaultdict, deque

graph = [[1, 3], [3], [], [2], []]


def dfs(g):
    if not g:
        return

    visited = {}

    for v in range(len(g)):
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
            for n in g[v]:
                if n not in visited:
                    queue.append(n)


dfs(graph)