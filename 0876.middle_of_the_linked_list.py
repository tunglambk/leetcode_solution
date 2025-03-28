# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        count = 0
        tmp = head
        while tmp != None:
            count += 1
            print(tmp.next)
            tmp = tmp.next

        middle = count // 2 + 1
        ret = head
        count2 = 1

        while count2 < middle:
            ret = ret.next
            count2 += 1

        return ret
    '''

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp1 = head
        tmp2 = head
        while tmp2 != None and tmp2.next != None:
            tmp1 = tmp1.next
            tmp2 = tmp2.next.next
        
        return tmp1
