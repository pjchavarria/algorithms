class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        result, dvd = "", n

        while dvd:
            result += chr((dvd-1)%26 + ord("A"))
            dvd = (dvd-1) / 26
        
        return result[::-1]
        

print Solution().convertToTitle(1), "A"
print Solution().convertToTitle(26), "Z"
print Solution().convertToTitle(27), "AA"
print Solution().convertToTitle(28), "AB"
print Solution().convertToTitle(52), "AZ"