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