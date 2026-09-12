# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeTwoLists(self, l1, l2):
        # logic for merging two lists
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val >= l2.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
            tail = tail.next

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return 
        if len(lists) == 1:
            return lists[0]

        i = 0
        k = len(lists) - 1

        while i != k:
            lists[i] = self.mergeTwoLists(lists[i], lists[k])
            k -= 1
        
        return lists[i]


# compare each node 