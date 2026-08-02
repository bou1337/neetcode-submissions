# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        fast  = head 
        slaw = head
        l1 = head
        while fast and fast.next:
            slaw = slaw.next
            fast  = fast.next.next
        
        l2 = slaw.next
        slaw.next =None
       
        prev = None
        nxt = None
        while l2:
            nxt = l2.next 
            l2.next = prev
            prev = l2
            l2=nxt
        r = head
        while prev:
            t1 = r.next 
            t2 = prev.next
            r.next = prev
            prev.next = t1 
            prev = t2
            r = t1 
    

