import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        dict = collections.defaultdict(list)

        for word in strs:
            ordered = "".join(sorted(word))
            dict[ordered].append(word)

        for anagram in dict.values():
            anagram.sort()
            result.append(anagram)

        return result

print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]), [
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]