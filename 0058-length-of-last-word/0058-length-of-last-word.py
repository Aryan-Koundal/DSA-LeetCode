class Solution(object):
    def lengthOfLastWord(self, s):
        a = s.split()
        for i in range(len(a)):
            if i == (len(a)-1):
                return len(a[i])