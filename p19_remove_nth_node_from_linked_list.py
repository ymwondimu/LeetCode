# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        curr = head
        count = 0
        while (curr and count < n):
            curr = curr.next
            count += 1

        if curr == None:
            return head.next

        prev = None
        slow = head

        while (curr):
            prev = slow
            slow = slow.next
            curr = curr.next

        prev.next = slow.next
        return head