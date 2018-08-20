# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None:
            return

        if head.next == None:
            return head

        curr = head
        prev = None

        while (curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev