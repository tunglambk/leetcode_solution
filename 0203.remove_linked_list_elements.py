# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return head
        
        new_head = head
        while new_head != None and new_head.val == val:
            new_head = new_head.next
        
        if new_head == None:
            return new_head

        tmp = new_head.next
        previous = new_head
        while tmp != None:
            if tmp.val == val:
                previous.next = tmp.next
            else:
                previous = tmp
            tmp = tmp.next
        return new_head
