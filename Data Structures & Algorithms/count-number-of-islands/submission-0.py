class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, column):
            if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0]):
                return
            if grid[row][column] == "0":
                return
            if grid[row][column] == "1":
                grid[row][column] = "0"
            
            dfs(row + 1, column)
            dfs(row - 1, column)
            dfs(row, column + 1)
            dfs(row, column - 1)

        res = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == "1":
                    dfs(row, column)
                    res += 1
        return res



                    