class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float('inf')
        max_profit = 0

        for price in prices:

            if price < min_price:
                min_price = price
            elif price - min_price > max_profit: 
                max_profit = price - min_price

        return max_profit

# if difference of price and prices[i - 1] is bigger than the difference of price and left, then append left
# if price > right, append right
# we always append right and then check 
