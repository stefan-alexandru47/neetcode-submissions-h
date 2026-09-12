class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1 
        
        while True:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]

            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            
        





# O(1) means the memory grows constantly as the algorithm runs 
# (ie input size shouldn't affect storage linearly or more)
# regular two sum solve creates an element in the dict with every iteration, which is O(n)
# for this solve, we must only reassign, and the category suggests we can use a two pointer startegy

# the input array is in increasing order, 
# which means the farthest items from the start may be higher than the target
# it would make most sense to compare the start and end items first
# if start and end go over target, the last number can be excluded
# same goes for any other numbers from end to start
# we can compare any numbers that aren't higher than target by addition 
# if left + right < target, move on to second left
# if left + right > target, move on to second right

# two pointers 

[3, 5, 8, 9, 10, 15]

target = 20
