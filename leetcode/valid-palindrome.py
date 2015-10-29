class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) == 0:
            return True

        validCharacters = "abcdefghijklmnopqrstuvwxyz1234567890"
        left = 0
        right = len(s)-1
        while left < right:
            leftString = s[left].lower()
            rightString = s[right].lower()
            moved = False
            if leftString not in validCharacters:
                left += 1
                moved = True
                
            if rightString not in validCharacters:
                right -= 1
                moved = True

            if leftString == rightString:
                left += 1
                right -= 1
                moved = True

            if not moved:
                print "a"
                return False

        if right - left <= 1 :
            return True
        else:
            print "b"
            return False

print Solution().isPalindrome("A man, a plan, a canal: Panama"), True
print Solution().isPalindrome("race a car"), False
print Solution().isPalindrome("1a2"), False
print Solution().isPalindrome("Red Roses run no risk "
    "sir "
    "on nurses order."), True