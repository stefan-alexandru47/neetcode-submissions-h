# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k) # 3 (num before next group)
            
            if not kth: # if kth is null, break and don't reverse group
                break   # ts is also the only way to break the loop

            groupNext = kth.next # head of next group

            prev, curr = kth.next, groupPrev.next
            while curr != groupNext: # 1's next becomes groupNext(4), 
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp 
                # 3's next will be 4 and we move to it so loop breaks

            tmp = groupPrev.next # 1
            groupPrev.next = kth # becomes 3
            groupPrev = tmp # becomes 1
        return dummy.next
            
        
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr