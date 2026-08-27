class Solution(object):

    def maxProfit(self, prices):

        x = prices[0]   # Minimum buying price
        y = 0           # Maximum profit

        for i in prices:

            if i < x:
                x = i

            profit = i - x

            if profit > y:
                y = profit

        return y