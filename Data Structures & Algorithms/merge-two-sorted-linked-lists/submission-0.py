# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1=list1
        ptr2=list2
        dummy=ListNode()
        dpointer=dummy
        while (ptr1!=None and ptr2!=None):
            if ptr1.val<ptr2.val:
                dpointer.next=ptr1
                ptr1=ptr1.next
            else:
                dpointer.next=ptr2
                ptr2=ptr2.next
            dpointer=dpointer.next
        
        if ptr1:
            dpointer.next=ptr1
        if ptr2:
            dpointer.next=ptr2
        
        return dummy.next
        
            



        