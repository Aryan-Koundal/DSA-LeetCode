class Solution(object):
    def countCommas(self, n):
        s = 0
        if n < 1000:
         s = 0
        else:
         s = n - 1000 + 1
        return s