# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l1 = head

        l2 = slow.next # this makes l2 be node in front of slow
        slow.next = None # this is to make l1's end be null, it make's slow point to null
        prev = None # this gives us a null value to give to the new end of the reversed list
        # so that l2 can also point toward null

        while l2:
            temp_next = l2.next
            l2.next = prev
            prev = l2
            l2 = temp_next

        l2 = prev

        while l2:
            tmp1, tmp2 = l1.next, l2.next
            l1.next = l2
            l2.next = tmp1
            l1, l2 = tmp1, tmp2

#[2, 4, 6]
#[10, 8]