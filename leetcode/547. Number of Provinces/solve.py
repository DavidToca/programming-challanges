NO_CONNECTION = 0


class Solution:
    def dfs(self, vertex, visited, g):
        visited[vertex] = True

        for neibourgh, is_on in enumerate(g[vertex]):
            if is_on == NO_CONNECTION:
                continue

            if visited[neibourgh]:
                continue

            self.dfs(neibourgh, visited, g)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        city_count = len(isConnected)

        visited = [False] * city_count

        connected = 0
        for vertex in range(city_count):

            if visited[vertex]:
                continue

            connected += 1

            self.dfs(vertex, visited, isConnected)

        return connected
