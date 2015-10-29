# https://leetcode.com/problems/word-break/

class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
        n = len(s)
        possible = [False for _ in xrange(n)]
        valid = [[False] * n for _ in xrange(n)]
        for i in xrange(n):
            if s[:i+1] in dict:
                possible[i] = True
                valid[0][i] = True
            for j in xrange(i):
                if possible[j] and s[j+1:i+1] in dict:
                    valid[j+1][i] = True
                    possible[i] = True
        print possible
        print valid
        result = []
        if possible[n-1]:
            self.genPath(s, valid, 0, [], result)
        return result
    
    def genPath(self, s, valid, start, path, result):
        if start == len(s):
            result.append(" ".join(path))
            return
        for i in xrange(start, len(s)):
            if valid[start][i]:
                path += [s[start:i+1]]
                self.genPath(s, valid, i + 1, path, result)
                path.pop()

        
print Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]), ["cats and dog", "cat sand dog"]
print Solution().wordBreak("a", ["a"]), ["a"]
print Solution().wordBreak("aaaaaaa", ["aaaa", "aa"]), []
print Solution().wordBreak("bb", ["a", "b", "bbb", "bbbb"]), ["b b"]

