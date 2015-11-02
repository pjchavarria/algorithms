# https://leetcode.com/problems/spiral-matrix-ii/

# Given an integer n, generate a square matrix filled with elements 
# from 1 to n2 in spiral order.

# For example,
# Given n = 3,

# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = []
        for i in xrange(n):
            matrix.append([0]*n)
        
        level = 0
        counter = 0
        num_of_levels = (n + 1 ) / 2
        while level < num_of_levels:
            counter = self.doSpiral(matrix, level, counter)
            level += 1

        return matrix


    def doSpiral(self, matrix, level, counter):
        level_column_max_idx = len(matrix)-level-1
        level_row_max_idx = len(matrix[0])-level-1
        # Loop first row
        for i in xrange(level, level_row_max_idx+1):
            counter += 1
            matrix[level][i] = counter

        # Append last element from level
        for i in xrange(level+1, level_column_max_idx):
            counter += 1
            matrix[i][level_row_max_idx] = counter

        # Loop last row in descending order
        if level_column_max_idx != level:
            for i in reversed(xrange(level, level_row_max_idx+1)):
                counter += 1
                matrix[level_column_max_idx][i] = counter
                
        # Append first element from level
        if level_row_max_idx != level:
            for i in reversed(xrange(level+1, level_column_max_idx)):
                counter += 1
                matrix[i][level] = counter

        return counter
        

print Solution().generateMatrix(0)
print Solution().generateMatrix(3)