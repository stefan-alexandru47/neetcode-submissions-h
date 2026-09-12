class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        product = 1
        zero_count = 0

        for i in range(length):
            if nums[i] == 0:
                zero_count += 1
            else:
                product = product * nums[i]

        res = []

        for num in nums:
            if zero_count > 1:
                res.append(0)
            elif zero_count == 1:
                if num == 0:
                    res.append(product)
                else:
                    res.append(0)
            else:
                res.append(product // num)

        return res

# get sufix and prefix product 


