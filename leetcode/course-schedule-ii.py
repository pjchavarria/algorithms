import collections

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        result, zeroInDegree, inDegree, outDegree = [], collections.deque(), {}, {}

        nodes = set()

        for edge in prerequisites:
            nodes.add(edge[0])
            nodes.add(edge[1])

        if len(nodes) != numCourses:
            return []

        self.buildGraph(prerequisites, inDegree, outDegree)

        for node in nodes:
            if node not in inDegree:
                zeroInDegree.append(node)

        
        while zeroInDegree:
            prerequisite = zeroInDegree.popleft()
            result.append(prerequisite)

            if prerequisite in outDegree:
                for node in outDegree[prerequisite]:
                    inDegree[node].discard(prerequisite)
                    if not inDegree[node]:
                        zeroInDegree.append(node)
                del outDegree[prerequisite]

        return result

    def buildGraph(self, prerequisites, inDegree, outDegree):
        for edge in prerequisites:
            nodeFrom = edge[1]
            nodeTo = edge[0]
            if nodeTo not in inDegree:
                inDegree[nodeTo] = set()
            if nodeFrom not in outDegree:
                outDegree[nodeFrom] = set()

            inDegree[nodeTo].add(nodeFrom)
            outDegree[nodeFrom].add(nodeTo)

print Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]), [0,1,2,3]
print Solution().findOrder(2, [[1,0]]), [0,1]