class Solution(object):
    def firstStableIndex(self, nums, k):
        a = []
        c = nums[:]
        b = 0
        for i in range(len(nums)):
          a.append(nums[i])
          b = (max(a)-min(c))
          if b <= k :
            return i
          if len(c) > 1 and nums[i] == c[0]:
             del c[0]
        return -1