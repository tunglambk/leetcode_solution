# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def _isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverseLinkedList(head: Optional[ListNode]) -> ListNode:
            if head == None or head.next == None:
                return head
            tmp = head.next
            reversed_list = reverseLinkedList(head.next)
            tmp.next = head
            head.next = None

            return reversed_list

        if not head or not head.next:
            return True
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, curr = None, slow
        reversed_list = reverseLinkedList(curr)

        while head and reversed_list:
            if head.val != reversed_list.val:
                return False
            head = head.next
            reversed_list = reversed_list.next
        return True
