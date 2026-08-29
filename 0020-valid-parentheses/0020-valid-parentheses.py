class Solution(object):
    def isValid(self, s):
        pairs = {
       ")": "(",
       "]": "[",
       "}": "{"
                }
        stack = []
        for i in s:
          if i == "(" or i == "[" or i == "{":
            stack.append(i)
          else:
            if not stack:
             return False
            if stack[-1] == pairs[i]:
             stack.pop()
            else:
             return False
        return len(stack) == 0