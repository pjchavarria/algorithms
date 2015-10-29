https://leetcode.com/problems/word-ladder-ii/
# BFS

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        count, current, visited = 0, [beginWord], set(beginWord)
        wordList.add(endWord)

        while current:
            results = []
            for word in current:
                if word == endWord:
                    return count + 1
                for i in xrange(len(beginWord)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + j + word[i+1:]
                        if candidate not in visited and candidate in wordList:
                            results.append(candidate)
                            visited.add(candidate)
            count += 1
            current = results

        return 0

print Solution().ladderLength("hit", "cog", set(["hot", "dot", "dog", "log", "lot", "log"]))