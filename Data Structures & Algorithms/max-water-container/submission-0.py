class Solution:
    def maxArea(self, heights: List[int]) -> int:

        j = 0
        k = len(heights) - 1
        res = 0

        while j < k:
            distance = k - j
            left = heights[j]
            right = heights[k]

            if left <= right:
                lowest_height = left
            else:
                lowest_height = right
            
            if distance * lowest_height > res:
                res = distance * lowest_height

            if left <= right:
                j = j + 1
            else:
                k = k - 1
        return res
    

# amount of water is based on lowest height of the two bars times distance between them 
# so we can do lowest height * distance between them 

# we can have one pointer at the start and one at the end
# range = right index - left index
# if left <= right: 
#    lowest_height = left
# else:
#    lowest_height = right
# for every left/right i, check if current range * lowest height > res, and append if so
# if left <= right:
#    left = left + 1
# else:
#    right = right - 1