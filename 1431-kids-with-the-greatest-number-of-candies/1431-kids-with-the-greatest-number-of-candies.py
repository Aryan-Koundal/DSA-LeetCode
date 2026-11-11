class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        x = [] * len(candies)
        for i in range(len(candies)):
             if candies[i]+extraCandies >= max(candies):
                x.append(True)
             else:
                x.append(False)
        return x