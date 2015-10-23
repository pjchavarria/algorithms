# https://leetcode.com/problems/maximum-depth-of-binary-tree/
#
from Queue import Queue

class TreeNode(object):
    def __init__(self, left=None, right=None):
        self.val = None
        self.left = left
        self.right = right

def maxDepth(root):
    if root:
        return max(height(root.left), height(root.right)) + 1
    return 0 



node4 = TreeNode()
node5 = TreeNode()
node3 = TreeNode(node4)
node2 = TreeNode(node5)
node1 = TreeNode(node2, node3)

print maxDepth(node1), 3
print maxDepth(node2), 2