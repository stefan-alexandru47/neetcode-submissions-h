class Solution:
    def search(self, nums: List[int], target: int) -> int:
        j, k = 0, len(nums) - 1

        while j < k:
            mid = (k + j) // 2

            if nums[mid] > nums[k]:
                j = mid + 1
            else: 
                k = mid
        n = j

        j, k = 0, len(nums) - 1
        
        while j <= k:
            mid = (k + j) // 2
            real_mid = (mid + n) % len(nums)
            if nums[real_mid] == target:
                return real_mid
            if nums[real_mid] > target:
                k = mid - 1
            else:
                j = mid + 1
        return -1
        
'''
algorithm that detects cutoff 
and treats the array as if it starts and ends at cutoff
it could be done by offsetting nums[i] by doing nums[i + n]

[3,4,5,6,1,2]

if min at index 4, n = 4, so if we want to access index 2, 
we have to access index 6 to get the correct value instead,
so we do nums[i + 4]

for numbers where i + 4 >= len(nums), we instead do :

i + 4 - len(nums)
'''