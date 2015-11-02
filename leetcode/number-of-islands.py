class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0

    
        for i in xrange(0, len(grid)):
            for j in xrange(0, len(grid[0])):
                if grid[i][j] == "1":
                    count = self.BFS(grid, i, j, count)

        return count

    def BFS(self, grid, i, j, count):

        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
            return count

        grid[i][j] = str(count+2)

        self.BFS(grid, i + 1, j, count)
        self.BFS(grid, i - 1, j, count)
        self.BFS(grid, i, j + 1, count)
        self.BFS(grid, i, j - 1, count)

        return count + 1


print Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]), 1
print Solution().numIslands([["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]]), 3
