# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head == None:
            return False

        if head.next == None:
            return False

        by_one = head
        by_two = head.next.next

        while (by_one and by_two):
            if by_one.val == by_two.val:
                return True
            else:
                if not by_two.next:
                    return False
                else:
                    by_one = by_one.next
                    by_two = by_two.next.next

        return False