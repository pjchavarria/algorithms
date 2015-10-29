import heapq
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return str(self.val)

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current = dummy
        heap = []
        for list in lists:
            if list:
                heapq.heappush(heap, (list.val, list))

        while heap:
            smallest = heapq.heappop(heap)[1]
            current.next = smallest
            current = smallest
            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, smallest.next))

        return dummy.next
            
        
list5 = ListNode(10)
list4 = ListNode(5)
list3 = ListNode(3)
list3.next = list4
list2 = ListNode(2)
list2.next = list5
list1 = ListNode(1)
list1.next = list3

result_list = Solution().mergeKLists([list1, list2])
while result_list:
    print result_list
    result_list = result_list.next