class Node:
    def __init__(self, leftNode, rightNode, value):
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.value = value
    def __repr__(self):
        return str(self.value)

def tree_inorder(root):
    if root is None:
        return []
    result = []
    result += tree_inorder(root.leftNode)
    result +=  [root]
    result += tree_inorder(root.rightNode)
    return result

def tree_preorder(root):
    if root is None:
        return []
    result = []
    
    result += [root]
    result += tree_preorder(root.leftNode)
    result += tree_preorder(root.rightNode)
    return result

def tree_postorder(root):
    if root is None:
        return []
    result = []

    result += tree_postorder(root.leftNode)
    result += tree_postorder(root.rightNode)
    result += [root]
    return result

node4 = Node(None, None, 4)
node5 = Node(node4, None, 5)
node2 = Node(None, None, 2)
node1 = Node(None, node2, 1)
node3 = Node(node1, node5, 3)
print tree_inorder(node3), [1,2,3,4,5]
print tree_preorder(node3), [3,1,2,5,4]
print tree_postorder(node3), [2,1,4,5,3]