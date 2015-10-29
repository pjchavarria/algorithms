class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return str(self.val)

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next

list4 = ListNode(3)
list3 = ListNode(2)
list3.next = list4
list1 = ListNode(1)
list1.next = list3


newHead =  Solution().reverseList(list1)

current = newHead
while current:
    print current
    current = current.next
