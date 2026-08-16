class Solution(object):
    def maximumWealth(self, accounts):
     maximum = 0
     for i in accounts :
         total = 0
         for j in i:
            total += j
         if total>maximum:
          maximum = total
     return maximum
