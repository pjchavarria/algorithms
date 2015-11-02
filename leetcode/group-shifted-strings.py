# https://leetcode.com/problems/group-shifted-strings/
# Given a string, we can "shift" each of its letter to its successive letter, 
# for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets, group all 
# strings that belong to the same shifting sequence.

# For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
# Return:

# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]
# Note: For the return value, each inner list's elements must follow the lexicographic order.

class Solution(object):
    def groupStrings(self, array):
        result = []
        dict = {
        "a":"b", "b":"c", "c":"d", "d":"e", "e":"f", "f":"g", "g":"h",
        "h":"i", "i":"j", "j":"k", "k":"l", "l":"m", "m":"n", "n":"o", 
        "o":"p", "p":"q", "q":"r", "r":"s", "s":"t", "t":"u", "u":"v", 
        "v":"w", "w":"x", "x":"y", "y":"z", "z":"a"}
        array.sort(reverse = True)
        while array:
            sequence = []
            element = array[len(array)-1]
            permutation = element
            while True:
                while permutation in array:
                    sequence.append(permutation)
                    array.remove(permutation)

                permutation = self.shift_string(permutation, dict)
                if permutation == element:
                    break
                
            if len(sequence):
                result.append(sequence)

        return result

    def shift_string(self, string, dict):
        newString = ""
        for i in string:
            newString += dict[i]
        return newString


print Solution().groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]), [
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]

print Solution().groupStrings(["a", "a"]), [
  ["a","a"]
]