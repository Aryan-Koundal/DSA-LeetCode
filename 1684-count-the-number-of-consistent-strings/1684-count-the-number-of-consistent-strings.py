class Solution(object):
    def countConsistentStrings(self, allowed, words):
        count = 0 
        for i in words:
            if all(char in allowed for char in i):
                count +=1
        return count