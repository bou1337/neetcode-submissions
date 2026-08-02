# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if  head==None or head.next == None:
            return False
        fast = head.next
        slaw  = head 

        while fast and fast.next:
            if(fast==slaw):
                return True
            fast=fast.next.next
            slaw = slaw.next
        
        return False 
        

