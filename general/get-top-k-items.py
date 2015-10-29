from heapq import heappush, heappop, heapify

# O(k+k+(n-k)*lon(k)) = O(2k+(n-k)*log(k)) = O(nlog(k))
# Space complexity = O(k+1) = O(k)
def getTopK(array, k):
    h = array[:k]
    heapify(h)

    for i in xrange(k, len(array)):
        heappush(h, array[i])
        heappop(h)
    return h

print "Get top k test cases"
print getTopK([1,2,3,5], 3), [2,3,5]
print getTopK([1,2,3,5], 4), [1,2,3,5]
print getTopK([1,2,3,5], 1), [5]
print getTopK([], 1), []

class Node:
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

# https://wiki.python.org/moin/TimeComplexity
# Time complexity = O(n*h*w) = O(n)
# Space complexity = O(kn)
def sumEachLevel(node):
    nextLevelArray = [node]
    result = []

    while nextLevelArray:
        levelArray = nextLevelArray
        nextLevelArray = []

        levelArrayValues = []
        for node in levelArray:
            levelArrayValues.append(node.value)
        result.append(getTopK(levelArrayValues, 1)[0])

        while levelArray:
            node = levelArray.pop()
            if node.left:
                nextLevelArray.append(node.left)
            if node.right:
                nextLevelArray.append(node.right)
        
    return result

childL2_1 = Node(None, None, 5)
childL2_2 = Node(None, None, 4)
childL2_3 = Node(None, None, 2)

childL1_1 = Node(childL2_1, childL2_2, 3)
childL1_2 = Node(childL2_3, None, 10)

root = Node(childL1_1, childL1_2, 11)

print "Sum each level test case"
print sumEachLevel(root), [11, 10, 5]
