class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        struct = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in struct:
                if [i < struct[diff]]:
                    return [struct[diff], i]
                else:
                    return [i, struct[diff]]
            else: 
                struct[num] = i
        return [0]

# have a hash map where you can store value and index pairs
# pass through array, and check for target - i
# we check map for the difference
# if found, we return i and index of the found value
