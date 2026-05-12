# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        # if len(lists) == 1:
        #     return lists[0]
        
        
        res = lists[0]
        
        def merger(list1, list2):
            mergedList = ListNode()
            head = mergedList
            while list1 and list2:
                if list1.val > list2.val:
                    mergedList.next = ListNode(list2.val)
                    list2 = list2.next
                else:
                    mergedList.next = ListNode(list1.val)
                    list1 = list1.next

                mergedList = mergedList.next


            if list1:
                mergedList.next = list1
            elif list2:
                mergedList.next = list2

            return head.next


        for i in range(1,len(lists)):
            res = merger(res, lists[i])
        
        return res

            