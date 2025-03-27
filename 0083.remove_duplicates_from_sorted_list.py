# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        tmp = head.next
        previous = head
        while tmp != None:
            if tmp.val == previous.val:
                previous.next = tmp.next
            else:
                previous = tmp
            tmp = tmp.next

        return head
