class Solution(object):
    def isSameAfterReversals(self, num):
        x = int(str(num)[::-1])
        y = int(str(x)[::-1])
        if num == y:
            return True
        return False