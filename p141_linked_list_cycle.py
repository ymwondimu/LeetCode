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
        by_two = head.next

        while (True):
            if by_two == None or by_two.next == None:
                return False
            if by_two == by_one or by_two.next == by_one:
                return True
            by_one = by_one.next
            by_two = by_two.next.next