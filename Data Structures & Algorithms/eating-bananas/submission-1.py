class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        j = 1
        k = max(piles)

        while j <= k:
            mid = (j + k) // 2
            hours = 0

            for num in piles:
                hours += math.ceil(num / mid)

            if hours <= h:
                k = mid - 1
            else: 
                j = mid + 1
        return j
