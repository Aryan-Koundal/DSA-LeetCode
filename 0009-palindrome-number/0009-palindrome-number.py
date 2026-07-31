class Solution:
    def isPalindrome(self, x: int) -> bool:
        d = str(x) 
        a = d[::-1]
        if d == a:
            return True
        elif d != a:
            return False 