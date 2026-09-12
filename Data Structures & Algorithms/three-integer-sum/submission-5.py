class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums) # [-4, -1, -1, 0, 1, 2]
        res = []
        
        for i, num in enumerate(sorted_nums): 
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            j = i + 1
            k = len(sorted_nums) - 1
            target = -num
        
            while j < k:
                if target == sorted_nums[j] + sorted_nums[k]:
                    res.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]]) 
                    # we append then skip current j & k to check every other pair (since we already checked current pair)
                    j += 1
                    k -= 1
                    # we need to check if new j & k are duplicates as well; if so, we skip them
                    while j < k and sorted_nums[j] == sorted_nums[j - 1]:
                        j += 1
                    while j < k and sorted_nums[k] == sorted_nums[k + 1]:
                        k -= 1
                    # j < k check guards against out of bounds j, which would throw an error when checking sorted_nums[j]

                elif sorted_nums[j] + sorted_nums[k] > target:
                    k -= 1
                else: 
                    j += 1
        return res