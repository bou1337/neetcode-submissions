# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fast = head 
        slaw = head
        if(head==None or head.next ==None):
            return None
        for  _ in range(n):
            fast=fast.next
        
        if fast is None:
            return head.next
        prev =None
        while fast:
            fast= fast.next
            prev = slaw
            slaw = slaw.next

        prev.next =slaw.next
        return head 