# You are given an array prices where prices[i]
# is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing
# a single day to buy one stock and choosing
# a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve
# from this transaction. If you cannot achieve any profit, return 0.

# Constraints:
#
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l_ind = 0
        res = 0
        for r_ind in range(1, len(prices)):
            if prices[r_ind] < prices[l_ind]:
                l_ind = r_ind
            res = max(res, prices[r_ind] - prices[l_ind])
        return res
