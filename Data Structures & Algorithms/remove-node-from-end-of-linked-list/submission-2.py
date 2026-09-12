# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head
        i = 0

        while curr:
            i += 1
            curr = curr.next

        curr = head
        index = i - n
        prev = ListNode()
        prev.next = curr
        j = 0

        while curr:
            if j == index:
                if j == 0:
                    head = curr.next
                else:
                    prev.next = curr.next
                    break
            else:
                prev = curr
                curr = curr.next
            j += 1
        return head