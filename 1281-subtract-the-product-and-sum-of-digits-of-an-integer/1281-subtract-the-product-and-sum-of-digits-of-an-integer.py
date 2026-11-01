class Solution(object):
    def subtractProductAndSum(self, n):
        num = 1
        count = 0
        while n >0:
           num *= n % 10
           count += n%10
           n //=10
        return num - count