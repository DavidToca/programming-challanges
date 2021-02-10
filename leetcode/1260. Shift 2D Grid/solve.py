class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        array_1d = []
        
        m = len(grid)
        n = len(grid[0])
        
        for arr1 in grid:
            array_1d.extend(arr1)
        
        print(array_1d)
        for _ in range(k):
            array_1d.insert(0, array_1d[-1])
            del array_1d[-1]
        
        arr_index = 0
        for i in range(m):
            for j in range(n):
                grid[i][j] = array_1d[arr_index]
                arr_index+=1
        return grid