EMPTY = 0
NOT_VISITED = 1
VISITED = 2


class Solution:
    def calculate_max_area(self, start_row, start_col, grid):
        cols = len(grid[0])
        rows = len(grid)

        stack = []

        stack.append((start_row, start_col))
        area = 0
        while stack:
            row, col = stack.pop()

            if row < 0 or row >= rows:
                continue
            if col < 0 or col >= cols:
                continue
            if grid[row][col] != NOT_VISITED:
                continue

            grid[row][col] = VISITED

            options = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            area += 1
            for deltax, deltay in options:
                stack.append((row + deltax, col + deltay))

        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        cols = len(grid[0])
        rows = len(grid)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == NOT_VISITED:
                    area = self.calculate_max_area(row, col, grid)
                    max_area = max(max_area, area)
        return max_area
