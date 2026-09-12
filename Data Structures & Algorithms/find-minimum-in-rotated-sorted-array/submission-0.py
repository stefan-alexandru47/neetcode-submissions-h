class Solution:
    def findMin(self, nums: List[int]) -> int:
        j = 0
        k = len(nums) - 1

        while j < k:
            mid = (k + j) // 2

            if nums[mid] > nums[k]:
                j = mid + 1
            else: 
                k = mid
        return nums[j]