class Solution(object):
    def maxProfit(self, prices):
        x = prices[0]
        y = 0
        for i in prices:
            if i <x:
                x =i
            if i-x> y:
                y  = i -x
        return y
        