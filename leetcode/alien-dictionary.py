# https://leetcode.com/problems/alien-dictionary/

# There is a new alien language which uses the latin alphabet. However, 
# the order among letters are unknown to you. You receive a list of words
# from the dictionary, where words are sorted lexicographically by the 
# rules of this new language. Derive the order of letters in this language.

# For example,
# Given the following words in dictionary,

# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
# The correct order is: "wertf".

# Note:
# You may assume all letters are in lowercase.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.
import collections

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        result, zero_in_degree_queue, in_degree, out_degree = [], collections.deque(), {}, {}

        nodes = set()
        for word in words:
            for c in word:
                nodes.add(c)

        for i in xrange(1, len(words)):
            self.findEdges(words[i-1], words[i], in_degree, out_degree)

        for node in nodes:
            if node not in in_degree:
                zero_in_degree_queue.append(node)

        while zero_in_degree_queue:
            precedence = zero_in_degree_queue.popleft()
            result.append(precedence)

            if precedence in out_degree:
                for c in out_degree[precedence]:
                    in_degree[c].discard(precedence)
                    if not in_degree[c]:
                        zero_in_degree_queue.append(c)
                del out_degree[precedence]

        if out_degree:
            return ""

        return "".join(result)

    def findEdges(self, word1, word2, in_degree, out_degree):
        str_len = min(len(word1), len(word2))
        for i in xrange(str_len):
            if word1[i] != word2[i]:
                if word2[i] not in in_degree:
                    in_degree[word2[i]] = set()
                if word1[i] not in out_degree:
                    out_degree[word1[i]] = set()

                in_degree[word2[i]].add(word1[i])
                out_degree[word1[i]].add(word2[i])
                break



print Solution().alienOrder([
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]), "wertf"

print Solution().alienOrder([
  "a",
  "b",
  "a"
]), ""

print Solution().alienOrder(["bsusz","rhn","gfbrwec","kuw","qvpxbexnhx","gnp","laxutz","qzxccww"])






