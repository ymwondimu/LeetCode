"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    #dummy head node in order to keep track of beginning of output
    head = ListNode(0)

    p1 = l1
    p2 = l2

    #list we will use to track values
    current = head

    #carry value
    carry = 0

    #While we have not reached end of either list, continue
    while ((p1 != None) and (p2 != None)):
        #set two values to be summed from list if available, otherwise 0
        sum1 = p1.val if p1 != None else 0
        sum2 = p2.val if p2 != None else 0

        #calculate the sum here, including carry value
        #set the new carry value
        sumtotal = sum1+sum2+carry
        carry = sumtotal//10

        #create a node with the new digit and point the current node to it
        current.next = ListNode(sumtotal%10)

        #move the current node over
        current = current.next

        #move the linked list for the numbers to be added over for the next digit sums
        p1 = p1.next
        p2 = p2.next

    #if there is a remaining carry value, tack it on
    if carry == 1:
        current.next = ListNode(carry)

    #return the beginning of the actual output by using the dummy head node created
    return head.next

def main():
    l1 = ListNode(2)
    l2 = ListNode(4)
    l3 = ListNode(3)
    l1.next = l2
    l2.next = l3

    r1 = ListNode(5)
    r2 = ListNode(6)
    r3 = ListNode(4)
    r1.next = r2
    r2.next = r3

    res = addTwoNumbers(l1, r1)

    while (res != None):
        print (res.val)
        res = res.next

if __name__ == "__main__":
    main()
