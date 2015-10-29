# https://leetcode.com/problems/contains-duplicate-ii/

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {}
        for idx, num in enumerate(nums):
            if dict.get(num, None):
                dict[num].append(idx)
                if self.indicesDifferenceIsAtMost(dict[num], k):
                    return True
            else:
                dict[num] = [idx]
        
        return False

    # Greedy solution
    def indicesDifferenceIsAtMost(self, array, k):

        if len(array) < 2:
            return False

        print array
        for index, value in enumerate(array[1:]):    
            candidate = value - array[index]
            if candidate <= k:
                return True

        return False


        
print Solution().containsNearbyDuplicate([1,2,1,4,3], 2), True
print Solution().containsNearbyDuplicate([1,2,1,4,3], 1), False
print Solution().containsNearbyDuplicate([1,0,1,1], 1), True