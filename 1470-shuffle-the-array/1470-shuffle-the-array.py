class Solution(object):
    def shuffle(self, nums, n):
       result = []
       for i in range(len(nums)//2):
          x = i + n
          result.append(nums[i])
          result.append(nums[x])
       return result