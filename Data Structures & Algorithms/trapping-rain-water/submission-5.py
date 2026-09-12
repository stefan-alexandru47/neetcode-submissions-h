class Solution:
    def trap(self, height: List[int]) -> int:
        j = 0
        k = len(height) - 1
        res = 0
        peak_j = height[j]
        peak_k = height[k]

        while j < k:
            if peak_j < peak_k:
                j += 1
                peak_j = max(peak_j, height[j])
                res += peak_j - height[j]
            else:
                k -= 1
                peak_k = max(peak_k, height[k])
                res += peak_k - height[k]

        return res