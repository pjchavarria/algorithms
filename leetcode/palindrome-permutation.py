# https://leetcode.com/problems/palindrome-permutation/
import collections
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        counter = collections.Counter()
        for character in s:
            counter[character] += 1
            if counter[character] >= 2:
                counter[character] -= 2

        result = sum(counter.values())
        if result == 1 or result == 0:
            return True
        else:
            return False        

print Solution().canPermutePalindrome("code"), False
print Solution().canPermutePalindrome("aab"), True
print Solution().canPermutePalindrome("carerac"), True
print Solution().canPermutePalindrome("aa"), True
print Solution().canPermutePalindrome("abc"), False