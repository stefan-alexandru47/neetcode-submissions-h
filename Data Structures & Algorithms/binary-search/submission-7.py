class Solution:
    def search(self, nums: List[int], target: int) -> int:
        j = 0
        k = len(nums) - 1

        while j <= k:
            mid = k - j // 2

            if nums[mid] == target:
                return mid
            
            if target > nums[mid]:
                j = mid + 1
            else:
                k = mid - 1
        return -1