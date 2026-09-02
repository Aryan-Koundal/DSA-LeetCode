class Solution(object):
    def isPalindrome(self, s):
        x=""
        for i in s:
            if i.isalnum():
                x +=i
        a = x[::-1].lower()
        x = x.lower()
        if x == a:
            return True
        return False 

        