import collections
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for array in board:
            counter = collections.Counter()
            for string in array:
                if not self.validateUniqueCharacters(counter, string):
                    return False

        for i in xrange(len(board)):
            counter = collections.Counter()
            for j in xrange(len(board)):
                string = board[j][i]
                if not self.validateUniqueCharacters(counter, string):
                    return False

        
        for i in xrange(0, 9, 3):
            for j in xrange(0, 9, 3):
                counter = collections.Counter()
                for k in xrange(3):
                    for l in xrange(3):
                        string = board[i+k][j+l]
                        if not self.validateUniqueCharacters(counter, string):
                            return False
        return True

    def validateUniqueCharacters(self, counter, string):
        if string is not ".":
            counter[string] += 1
            if counter[string] > 1:
                return False
        return True


        

print Solution().isValidSudoku([
    "53..7....",
    "6..195...",
    ".98....6.",
    "8...6...3",
    "4..8.3..1",
    "7...2....",
    ".6....28.",
    "...419..5",
    "....8..79"
    ]), True

print Solution().isValidSudoku([
    "53..7....",
    "6..195...",
    ".98....6.",
    "8...6...3",
    "4..8.3..1",
    "7...2....",
    ".3....28.",
    "...419..5",
    "....8..79"
    ]), False

print Solution().isValidSudoku([
    "53..7....",
    "6..195...",
    ".99....6.",
    "8...6...3",
    "4..8.3..1",
    "7...2....",
    ".6....28.",
    "...419..5",
    "....8..79"
    ]), False

print Solution().isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]), True