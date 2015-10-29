# https://leetcode.com/problems/word-break/

class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
    
    if
        counter = {}

        for i in s:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1

        for c in s:
            if c not in counter:
                return False

        n = len(s)
        possible = [False for _ in s]

        for i in xrange(n):
            for j in reversed(xrange(i+1)):
                if (j == 0 or possible[j-1]) and s[j:i+1] in dict:
                    possible[i] = True
                    break

        return possible[n-1]

        
print Solution().wordBreak("leetcode", ["leet", "code"]), True
print Solution().wordBreak("leetcode", ["leet", "cowe"]), False
print Solution().wordBreak("aleetacowe", ["leet", "cowe", "a"]), True
print Solution().wordBreak("aleetacoaea", ["leet", "cowe", "a"]), False
