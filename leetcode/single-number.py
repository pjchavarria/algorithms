#https://leetcode.com/problems/single-number/

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(operator.xor, nums)


print Solution().singleNumber([2,2,1,3,3])