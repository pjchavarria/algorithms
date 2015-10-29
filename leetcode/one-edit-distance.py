# https://leetcode.com/problems/one-edit-distance/

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        idxS = 0
        idxT = 0
        
        lenS = len(s)
        lenT = len(t)

        changes = 0

        if lenS == 0 and lenT == 0:
            return False
        if (lenS == 0 and lenT == 1) or (lenS == 1 and lenT == 0):
            return True

        while idxT < lenT or idxS < lenS:
            if idxS < lenS and idxT < lenT and s[idxS] == t[idxT]:
                idxS += 1
                idxT += 1
            else:
                if idxT+1 < lenT and idxS < lenS and s[idxS] == t[idxT+1]:
                    idxT += 1
                    changes += 1
                elif idxS+1 < lenS and idxT < lenT and t[idxT] == s[idxS+1]:
                    idxS += 1
                    changes += 1
                else:
                    if idxS != lenS:
                        idxS += 1
                    if idxT != lenT:
                        idxT += 1
                    changes += 1

            if changes > 1:
                return False

        if changes == 1:
            return True
        else:
            return False
        

print Solution().isOneEditDistance("car", "bar"), True
print Solution().isOneEditDistance("car", "ber"), False
print Solution().isOneEditDistance("car", "be"), False
print Solution().isOneEditDistance("car", "ca"), True
print Solution().isOneEditDistance("", ""), False
print Solution().isOneEditDistance("", "a"), True
print Solution().isOneEditDistance("car", "cab"), True

print Solution().isOneEditDistance("ba", "a"), True