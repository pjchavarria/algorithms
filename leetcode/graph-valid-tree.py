# https://leetcode.com/problems/graph-valid-tree/

# Given n nodes labeled from 0 to n - 1 and a list of undirected edges 
# (each edge is a pair of nodes), write a function to check whether these
# edges make up a valid tree.

# For example:

# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

# Hint:

# Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], what should your return? 
# Is this case a valid tree? Show More Hint 
# Note: you can assume that no duplicate edges will appear in edges. Since 
# all edges are undirected, [0, 1] is the same as [1, 0] and thus will not 
# appear together in edges.
import collections

class Solution(object):
    def validTree(self, n, edges):
        if len(edges) != n - 1:  # Check number of edges.
            return False
        elif n == 1:
            return True

        visited_from, neighbors = 0, 1

        # A structure to track each node's [visited_from, neighbors]
        nodes = collections.defaultdict(lambda: [-1, []])

        for edge in edges:
            nodes[edge[0]][neighbors].append(edge[1])
            nodes[edge[1]][neighbors].append(edge[0])

        if len(nodes) != n:  # Check number of nodes.
            print "c"
            return False

        # BFS to check whether the graph is valid tree.
        visited = {}
        q = collections.deque()
        q.append(0)
        while q:
            i = q.popleft()
            visited[i] = True
            for node in nodes[i][neighbors]:
                if node != nodes[i][visited_from]:
                    if node in visited:
                        return False
                    else:
                        visited[node] = True
                        nodes[node][visited_from] = i
                        q.append(node)
        return len(visited) == n


print Solution().validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]), True
print Solution().validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]), False
print Solution().validTree(4, [[0, 1], [2, 3]]), False


