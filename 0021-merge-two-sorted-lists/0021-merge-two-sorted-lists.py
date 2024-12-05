# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        tail = head
        while(list1 is not None and list2 is not None):
            if list1.val <= list2.val:
                tail.next = list1 #fixed it from list1.val to list1
                list1 = list1.next
            else:
                tail.next = list2 #fixed it from list2.val to list2
                list2 = list2.next
            tail = tail.next
        
        #add any remaining elements either from list1 or list2:
        if list1 is not None:
            tail.next = list1
        elif list2 is not None:
            tail.next = list2
        
        return head.next #fixed it from head to head.next
        #recursion solution
        #if list1 is None:
        #    return list2
        #if list2 is None:
        #    return list1

        #if list1.val <= list2.val: 
        #    list1.next = self.mergeTwoLists(list1.next, list2)
        #    return list1
        #else:
        #    list2.next = self.mergeTwoLists(list1, list2.next)
        #    return list2
