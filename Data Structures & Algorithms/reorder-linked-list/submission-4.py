# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        one = head
        two = slow.next
        slow.next = None
        prev = None

        while two:
            tmp_next = two.next
            two.next = prev
            prev = two
            two = tmp_next

        two = prev
        
        while two:
            tmp_next_1 = one.next
            tmp_next_2 = two.next
            one.next = two
            two.next = tmp_next_1
            one = tmp_next_1
            two = tmp_next_2

        

        
# [2,4,6,8,10]

# [2, 4, 6]
# [10, 8]
# find half of list using slow fast alg
# reverse middle of list + 1
# merge using temp_nexts