# https://leetcode.com/problems/spiral-matrix/

# Given a matrix of m x n elements (m rows, n columns), 
# return all elements of the matrix in spiral order.

# For example,
# Given the following matrix:

# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not len(matrix):
            return []
        result = []
        level = 0
        num_of_levels = (min(len(matrix), len(matrix[0])) + 1 ) / 2
        while level < num_of_levels:
            self.doSpiral(matrix, result, level)
            level += 1

        return result


    def doSpiral(self, matrix, result, level):
        level_column_max_idx = len(matrix)-level-1
        level_row_max_idx = len(matrix[0])-level-1
        # Loop first row
        for i in xrange(level, level_row_max_idx+1):
            result.append(matrix[level][i])

        # Append last element from level
        for i in xrange(level+1, level_column_max_idx):
            result.append(matrix[i][level_row_max_idx])

        # Loop last row in descending order
        if level_column_max_idx != level:
            for i in reversed(xrange(level, level_row_max_idx+1)):
                result.append(matrix[level_column_max_idx][i])        
                
        # Append first element from level
        if level_row_max_idx != level:
            for i in reversed(xrange(level+1, level_column_max_idx)):
                result.append(matrix[i][level])
        

print Solution().spiralOrder([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
])

print Solution().spiralOrder([
 [ 1, 2, 3, 4],
 [ 5, 6, 7, 8 ],
 [ 9, 10, 11, 12 ],
 [ 13, 14, 15, 16]
])

print Solution().spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])

print Solution().spiralOrder([
 [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
])

print Solution().spiralOrder([
 [1], [2], [3]
])