# https://leetcode.com/problems/combination-sum/

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.backtrack(candidates, [], result, target)
        return result
        
    def backtrack(self, candidates, buildup, result, target):

        #print buildup
        value = 0
        for i in buildup:
            value += i
        if value > target:
            return
        if value == target:
            found = False
            buildup.sort()
            for array in result:
                if array == buildup:
                    found = True
            if not found:
                result.append(buildup)

        for candidate in candidates:
            self.backtrack(candidates, buildup+[candidate], result, target)



print Solution().combinationSum([6,8,12,5,9,3,4,11], 31), [[7], [2,2,3]]