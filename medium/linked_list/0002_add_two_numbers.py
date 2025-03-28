# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None, previous=None):
        self.val = val
        self.next = next
        self.previous = previous
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        quotient = 0
        head = current = ListNode(0)
        while l1 or l2:
            val = quotient
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            
            mod = val%10
            quotient = val//10
            current.val = mod
            current.next = ListNode(0, previous=current)
            current = current.next
        if quotient > 0:
            current.val = quotient
        if current.val == 0:
            current.previous.next = None
        return head
