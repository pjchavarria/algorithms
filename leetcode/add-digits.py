# https://leetcode.com/problems/add-digits/

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return (num - 1) % 9 + 1 if num > 0 else 0


print Solution().addDigits(38), 2
print Solution().addDigits(100), 1
print Solution().addDigits(4), 4
