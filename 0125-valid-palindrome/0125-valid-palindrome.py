class Solution(object):
    def isPalindrome(self, s):
        x=""
        for i in s:
            if i.isalnum():
                x +=i
        x = x.lower()
        a = x[::-1]
        if x == a:
            return True
        return False 

        