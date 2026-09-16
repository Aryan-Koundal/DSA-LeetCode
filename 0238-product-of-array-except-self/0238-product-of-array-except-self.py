class Solution(object):
    def productExceptSelf(self, nums):
        x =[]
        product = 1
        for i in range(len(nums)):
            x.append(product)
            x[i] = product
            product = product * nums[i] 

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            x[i] = x[i] * product
            product = product * nums[i]
        return x