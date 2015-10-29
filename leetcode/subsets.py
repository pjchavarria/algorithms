# https://leetcode.com/problems/subsets/

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = [[]]
        self.backtrack(nums, result)
        return result

    def backtrack(self, nums, result):
        if len(nums) == 0:
            return []
        result.append(nums)

        for i in xrange(len(nums)):
            newSet = nums[:i]+nums[i+1:]  
            if newSet not in result:  
                self.backtrack(newSet, result)


print Solution().subsets([1,2,3])
print [
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]