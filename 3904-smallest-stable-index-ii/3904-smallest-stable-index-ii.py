class Solution(object):
    def firstStableIndex(self, nums, k):
        left_max = [0] * len(nums)
        left_max[0] = nums[0]
        for i in range(1, len(nums)):
            left_max[i] = max(nums[i], left_max[i - 1])
        suffix_min = [0] * len(nums)
        suffix_min[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])
        for i in range(len(nums)):
            if left_max[i] - suffix_min[i] <= k:
                return i
        return -1     