# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        two = head

        for i in range(n):
            two = two.next
            
        one = dummy

        while two:
            one = one.next
            two = two.next

        one.next = one.next.next
        return dummy.next