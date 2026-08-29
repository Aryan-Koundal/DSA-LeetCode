class Solution(object):
    def moveZeroes(self, nums):
        result =[]
        x = []
        for i in nums:
            if i!=0:
                result.append(i)
            if i == 0:
                x.append(i)
        result.extend(x)
        nums[:]=result
        