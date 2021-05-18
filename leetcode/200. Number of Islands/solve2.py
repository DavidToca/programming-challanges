class Solution:
    def dfs(self, row, col, grid):
        if row < 0 or row >= len(grid):
            return
        if col < 0 or col >= len(grid[0]):
            return
        if grid[row][col] != '1':
            return
        grid[row][col] = '2'
        
        adjacents = [
            (row, col-1),
            (row, col+1),
            (row-1, col),
            (row+1, col),
        ]
        for position in adjacents:
            row, col = position
            self.dfs(row, col, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != '1':
                    continue
                
                num_islands +=1
                self.dfs(row, col, grid)
        return num_islands