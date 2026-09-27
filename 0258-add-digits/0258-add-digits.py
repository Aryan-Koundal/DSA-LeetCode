class Solution(object):
    def addDigits(self, num):
      while num >= 10:
        a = 0
        while num > 0:
            x = num%10
            a = a + x
            num //=10
        num = a
      return num
      