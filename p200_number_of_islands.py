class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        if len(grid) == 0:
            return 0

        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.dfs(i, j, grid)
                    count += 1

        return count

    def dfs(self, i, j, grid):
        grid[i][j] = "#"
        neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for neighbor in neighbors:
            new_i, new_j = i + neighbor[0], j + neighbor[1]
            if check_boundary(new_i, new_j, grid) and grid[new_i][new_j] == "1":
                self.dfs(new_i, new_j, grid)


def check_boundary(i, j, grid):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return False
    return True
