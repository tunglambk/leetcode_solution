# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        tmp = head.next
        reverse_list = self.reverseList(head.next)
        tmp.next=head
        head.next=None
        return reverse_list
