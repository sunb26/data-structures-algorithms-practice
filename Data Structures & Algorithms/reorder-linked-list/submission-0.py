# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # get the halfway point of the list
        p1 = head
        p2 = head.next

        while p2 and p2.next:
            p2 = p2.next.next
            p1 = p1.next

        # p1 should be halfway now. Reverse the second half of the list

        second = p1.next
        prev = p1.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
            
        
        # Re-order
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            second = tmp2
            first = tmp1
        
        

