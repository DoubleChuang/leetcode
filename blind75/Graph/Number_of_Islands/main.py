class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid: List[List[str]], x: int, y: int, m: int, n: int):
            if x < 0 or y < 0: return
            if x >= m or y >= n: return
            if grid[x][y] == '0': return
            
            grid[x][y] = '0'

            dfs(grid, x+1, y, m, n)
            dfs(grid, x-1, y, m, n)
            dfs(grid, x, y+1, m, n)
            dfs(grid, x, y-1, m, n)
            
        
        m = len(grid)
        n = len(grid[0])

        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(grid, i, j, m, n)

        return islands