HAS_ISLAND = '1'
MARKED = '2'

class Solution:
    def dfs(self, row, col, grid):
        stack = []        
        stack.append((row, col))

        while stack:
            row, col = stack.pop()
            if row < 0 or row >= len(grid):
                continue
            if col < 0 or col >= len(grid[0]):
                continue
            if grid[row][col] != HAS_ISLAND:
                continue
            grid[row][col] = MARKED
        
            adjacents = [
                (row, col-1),
                (row, col+1),
                (row-1, col),
                (row+1, col),
            ]
            for position in adjacents:
                row, col = position
                stack.append((row, col))

    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        stack = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != HAS_ISLAND:
                    continue
                
                num_islands +=1
                self.dfs(row, col, grid)

                    
        return num_islands