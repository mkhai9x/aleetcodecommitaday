from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left, right = 0, 0
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                profit = max(profit, prices[right] - prices[left])
            right += 1
        return profit


prices = [7, 1, 5, 3, 6, 4]

prices = [7, 6, 4, 3, 1]
print(Solution().maxProfit(prices))
