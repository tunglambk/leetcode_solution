class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = prices[0]
        for current_price in prices[1:]:
            if current_price < min_price:
                min_price = current_price
            elif current_price - min_price > max_profit:
                max_profit = current_price - min_price
        return max_profit
