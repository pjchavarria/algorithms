# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # dict = {
        # "2":["a","b","c"],
        # "3":["d","e","f"],
        # "4":["g","h","i"],
        # "5":["j","k","l"],
        # "6":["m","n","o"],
        # "7":["p","q","r","s"],
        # "8":["t","u","v"],
        # "9":["w","x","y","z"]
        # }

        # array = []
        # for i in digits:
        #     array.append(dict[i])

        # result = []
        # self.backtrack(array, result)


        return [None]*2

    def backtrack(self, array, result):

        for i in array:            
            print i

        #self.backtrack(sub_element, array, result)

print Solution().letterCombinations("23")