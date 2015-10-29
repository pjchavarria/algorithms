# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left, right = 0, len(nums)

        while left < right:

            mid = left + (right-left)/2   

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:
                if nums[mid] > target and nums[left] <= target:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and nums[right-1] >= target:
                    left = mid + 1
                else:
                    right = mid 

        return -1

        




print Solution().search([4,5,6,7,0,1,2], 5), 1
print Solution().search([1], 1), 0
print Solution().search([3,5,7], 3), 0
print Solution().search([1], 0), -1
print Solution().search([1,3], 0), -1
print Solution().search([1,3], 3), 1
print Solution().search([3, 1], 3), 0
print Solution().search([4,5,6,7,0,1,2], 1), 5
print Solution().search([4,5,6,7,0,1,2], 0), 4
print Solution().search([4,5,6,7,8,1,2,3], 8), 4
print Solution().search([5,1,3], 3), 2