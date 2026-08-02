# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head==None or head.next==None  or head.next.next==None:
            return False
        
        slaw =  head 
        fast =  head.next

        while slaw  and fast and fast.next:

            if(slaw==fast):
                return True
            slaw = slaw.next
            fast = fast.next.next
        
        return False 

