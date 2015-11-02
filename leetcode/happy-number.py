# https://leetcode.com/problems/happy-number/
# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Example: 19 is a happy number

# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        results = {}
        loop_count = 0
        while n != 1:
            sum = 0
            for i in str(n):
                sum += int(i) * int(i)
            n = sum
            loop_count +=1
            if results.get(n, None) is not None or loop_count == 100:
                break

        return True if n == 1 else False


print Solution().isHappy(19), True
print Solution().isHappy(20), False
print Solution().isHappy(68), True
print Solution().isHappy(100), True
print Solution().isHappy(1), True
print Solution().isHappy(2147483647), True
