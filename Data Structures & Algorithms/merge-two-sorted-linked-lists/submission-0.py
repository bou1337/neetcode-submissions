# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        result  = ListNode()
        curr = result

        while list1 and list2:

            if list1.val>list2.val:
                mn = list2.val
                list2=list2.next
            else:
                mn = list1.val
                list1 = list1.next
            tmp = ListNode(mn,None)
            curr.next = tmp 
            curr = curr.next
        
        while list2:
            tmp = ListNode(list2.val)
            curr.next = tmp 
            curr = curr.next
            list2=list2.next

        while list1:
            tmp = ListNode(list1.val)
            curr.next = tmp 
            curr = curr.next
            list1=list1.next
        return result.next    
        