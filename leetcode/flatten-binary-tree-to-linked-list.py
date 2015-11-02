# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Given a binary tree, flatten it to a linked list in-place.

# For example, given:
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6

# The flattened tree should look like:

#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6


# Thoughts
# Go down through the lef t, when right is not null, push right to stack.

class TreeNode:
    def __init__(self, val = 0, left = null, right = null):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

node6 = TreeNode(6)
node5 = TreeNode(5, null, node6)
node4 = TreeNode(4)
node3 = TreeNode(3)
node2 = TreeNode(2, node3, node4)
node1 = TreeNode(1, node2, node5)

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        stack = [root]

        while stack:
            root = stack.pop()
            if root.right and root.left:
                stack.append(root.right)
                root.right = root.left
                stack.append(root.right)
            elif stack:
                last = stack[len(stack)-1]
                root.right = last



        

Solution().flatten(node1)

root = node1
while root:
    print root
    root = root.right



