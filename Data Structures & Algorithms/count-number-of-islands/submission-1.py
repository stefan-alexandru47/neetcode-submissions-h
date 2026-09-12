class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, column = len(grid), len(grid[0])
        islands = 0


        def dfs(r, c):
            if r < 0 or r > row - 1 or c < 0 or c > column - 1 or grid[r][c] != '1':
                return

            grid[r][c] = '0'
            dfs(r, c+1)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r-1,c)


        for r in range(row):
            for c in range(column):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)
        
        return islands
    







        
        
"""======================================)
|  𓇳  𓆣  𓏥  𓇋  𓏠  𓈖  𓋹  𓋾  𓉺  𓇌  𓊖   |
(========================================)

go through each node
at 1's, if wasd 


(========================================)
|  𓇳  𓆣  𓏥  𓇋  𓏠  𓈖  𓋹  𓋾  𓉺  𓇌  𓊖   |
(======================================"""