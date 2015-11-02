class Solution(object):
    def numOfAreas(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        formatted_grid = []
        
        # Create grid
        for row in grid:
            string1 = []
            string2 = []
            string3 = []
            for element in row:
                if element == "\\":
                    string1 += ["0","1","1"]
                    string2 += ["1","0","1"]
                    string3 += ["1","1","0"]
                else:
                    string1 += ["1","1","0"]
                    string2 += ["1","0","1"]
                    string3 += ["0","1","1"]

            formatted_grid.append(string1)
            formatted_grid.append(string2)
            formatted_grid.append(string3)

        for i in xrange(0, len(formatted_grid)):
            for j in xrange(0, len(formatted_grid[0])):
                if formatted_grid[i][j] == "1":
                    count = self.BFS(formatted_grid, i, j, count)

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


print Solution().numOfAreas([
    ["\\","\\","/"],
    ["/","\\","/"],
    ["\\","\\","\\"],
    ["/","/","/"],
    ["\\","\\","\\"]])
