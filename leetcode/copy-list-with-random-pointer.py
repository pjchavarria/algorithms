class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dummy = RandomListNode(0)
        current, dict, prev = head, {}, dummy

        while current:
            copy = RandomListNode(current.label)
            dict[current] = copy
            prev.next = copy
            prev, current = prev.next, current.next

        current = head

        while current:
            if current.random:
                dict[current].random = dict[current.random]
            current = current.next

        return dummy.next


head = RandomListNode(1)
head.next = RandomListNode(2)
head.random = head.next
result = Solution().copyRandomList(head)
print result.label
print result.next.label
print result.random.label