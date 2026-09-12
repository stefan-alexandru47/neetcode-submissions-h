class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minimum = float('inf')
        max_profit = 0

        for price in prices:

            if price < minimum:
                minimum = price
            elif price - minimum > max_profit:
                max_profit = price - minimum
                
        return max_profit

        # minimum always gets appended
        # but max_profit doesn't get appended unless i's profit is bigger than your biggest profit

        # [10, 1, 5, 6, 7, 0]
        # 0 will not have any effect, 
        # as minimum will be appended, but max_profit is bigger than 0 - 0 (price - minimum)
        # we keep track of max_profit, NOT MAX, and minimum always gets appended first
        
# track a minimum
# track a max profit
# update minimum first as you first need to buy in order to have a profit

# minimum has to start as high as possible so whatever you update first is always smaller, to take its place