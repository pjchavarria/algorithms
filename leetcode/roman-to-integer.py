# https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numeral_map = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        decimal = 0
        for i in xrange(len(s)):
            if i > 0 and numeral_map[s[i]] > numeral_map[s[i - 1]]:
                decimal += numeral_map[s[i]] - 2 * numeral_map[s[i - 1]]
            else:
                decimal += numeral_map[s[i]]
        return decimal
        
print Solution().romanToInt("I"), 1
print Solution().romanToInt("IV"), 4
print Solution().romanToInt("V"), 5
print Solution().romanToInt("VI"), 6
print Solution().romanToInt("VII"), 7
print Solution().romanToInt("VIII"), 8
print Solution().romanToInt("IX"), 9
print Solution().romanToInt("X"), 10
print Solution().romanToInt("XXXV"), 35
print Solution().romanToInt("L"), 50
print Solution().romanToInt("C"), 100
print Solution().romanToInt("D"), 500
print Solution().romanToInt("M"), 1000

