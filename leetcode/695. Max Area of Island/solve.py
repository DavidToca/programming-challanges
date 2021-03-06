EMPTY = 0
NOT_VISITED = 1
VISITED = 2


class Solution:
    def calculate_max_area(self, row, col, grid):
        cols = len(grid[0])
        rows = len(grid)

        if row < 0 or row >= rows:
            return 0
        if col < 0 or col >= cols:
            return 0
        if grid[row][col] != NOT_VISITED:
            return 0

        grid[row][col] = VISITED

        options = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        area = 1
        for deltax, deltay in options:
            area += self.calculate_max_area(row + deltax, col + deltay, grid)

        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        m = len(grid[0])
        n = len(grid)

        for row in range(n):
            for col in range(m):
                if grid[row][col] == NOT_VISITED:
                    area = self.calculate_max_area(row, col, grid)
                    max_area = max(max_area, area)
        return max_area
