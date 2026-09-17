class Solution(object):
    def topKFrequent(self, nums, k):
        dictionary = {}
        x =[]
        for i in nums:
         if i in dictionary:
           dictionary[i] = dictionary[i] + 1
         else:
           dictionary[i] = 1 
        x= sorted(dictionary, key=dictionary.get, reverse=True)[:k]
        return x