class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = {}
        for num in nums:
            if dict.get(num, None):
                return True
            dict[num] = True
        return False
        

print Solution().containsDuplicate([1,2,3,4]), False
print Solution().containsDuplicate([1,2,1,4]), True