class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        
        def dfs(r, c): 
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return 0

            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            return dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1) + 1

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 1:
                    maxArea = max(maxArea, dfs(row, column))
        
        return maxArea