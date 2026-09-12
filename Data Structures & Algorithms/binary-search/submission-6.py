class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            middle = (start + end) // 2
            if nums[middle] == target:
                return middle
            elif target < nums[middle]: # if smaller than middle, start stays same, end changes to middle
                end = middle - 1 # new end = old middle
            elif target >= nums[middle]:
                start = middle + 1
        return -1

# set start and end
# look at the middle of array
# if target smaller than number, move to lower middle, 
# if targe bigger, move to upper middle
# to do so, set start to middle, and end to 0 or -1, in the first iteration for example

# middle will always be 
# to reach target: