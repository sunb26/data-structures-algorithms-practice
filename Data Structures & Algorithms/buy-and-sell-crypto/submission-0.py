class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        buy, sell = 0, 1
        max_profit = 0
        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if prices[buy] > prices[sell]:
                buy = sell
            sell += 1
            max_profit = max(max_profit, profit)
        return max_profit
