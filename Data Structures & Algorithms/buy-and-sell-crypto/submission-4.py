class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        max_profit = 0

        for num in prices:
            if num < low:
                low = num
            if num - low > max_profit:
                max_profit = num - low
        return max_profit
