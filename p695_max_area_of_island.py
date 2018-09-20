class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        self.count = 0
        max_count = 0

        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    self.count = 0
                    self.dfs(i, j, grid)
                    max_count = max(max_count, self.count)

        return max_count

    def dfs(self, i, j, grid):
        if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == 1:
            grid[i][j] = 0
            self.count += 1
            self.dfs(i - 1, j, grid)
            self.dfs(i + 1, j, grid)
            self.dfs(i, j - 1, grid)
            self.dfs(i, j + 1, grid)