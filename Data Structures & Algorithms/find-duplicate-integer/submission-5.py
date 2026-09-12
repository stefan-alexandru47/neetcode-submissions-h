class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break

        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if fast == slow:
                return slow
# if you treat the array as a linked list, where .next is instead []

# [3, 6, 4, 1, 2, 5, 3]
# 1[3] - > 2[1] - > 3[6] - > 4[3]