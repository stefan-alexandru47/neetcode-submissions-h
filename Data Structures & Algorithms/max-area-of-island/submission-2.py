class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0]) 
        max_area = 0

        def dfs(r, c):
            if r < 0 or r > rows-1 or c < 0 or c > columns-1 or grid[r][c] != 1:
                return 0

            grid[r][c] = 0

            right = dfs(r, c+1)
            down = dfs(r+1, c)
            left = dfs(r, c-1)
            up = dfs(r-1, c)

            return 1 + right + down + left + up
        
        for r in range(rows):
            for c in range(columns):
                curr_area = dfs(r, c)
                max_area = max(max_area, curr_area)

        return max_area


"""======================================)
|  𓇳  𓆣  𓏥  𓇋  𓏠  𓈖  𓋹  𓋾  𓉺  𓇌  𓊖   |
(========================================)

for this problem, all we need to do is
to make a dfs that returns area.
we do (for r and c), and for each, we 
simply recursively keep a counter by
returning (1 + counter) with every function
the for-loop grabs that and reassigns
a max_area var of the enclosing function

to implement the (1 + counter) return here
we can call each direction after a variable:
curr_area += dfs(r+1, c)
to append either 1 or 0 based on the return
and ofc we code water to return 0 and land 1

(========================================)
|  𓇳  𓆣  𓏥  𓇋  𓏠  𓈖  𓋹  𓋾  𓉺  𓇌  𓊖   |
(======================================"""