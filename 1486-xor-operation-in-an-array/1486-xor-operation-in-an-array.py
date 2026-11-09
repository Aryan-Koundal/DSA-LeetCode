class Solution(object):
    def xorOperation(self, n, start):
        nums = 0
        for i in range(n):
            nums ^= start + 2 * i
        return nums