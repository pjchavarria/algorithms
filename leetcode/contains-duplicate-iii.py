# https://leetcode.com/problems/contains-duplicate-iii/
from collections import OrderedDict

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 0 or t < 0:
            return False
        window = OrderedDict()
        for n in nums:
            # Make sure window size
            print "window"
            print window
            if len(window) > k:
                print "Popping item from window"                
                window.popitem(False)
                
            bucket = n if not t else n // t
            print "bucket"
            print bucket
            # At most 2t items.
            for m in (window.get(bucket - 1), window.get(bucket), window.get(bucket + 1)):
                if m is not None and abs(n - m) <= t:
                    print "abs(n - m) <= t"
                    return True
            window[bucket] = n
        return False

        
print Solution().containsNearbyAlmostDuplicate([4,30,1,6,2], 2, 1), True
print "-"*10
print Solution().containsNearbyAlmostDuplicate([1,3,5,8,10], 1, 1), False
